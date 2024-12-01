from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import buttons
import random
from db.db_main import sql_insert_products
from google_sheets.sheets import update_google_sheets


class reg(StatesGroup):
    code = State()
    fullname = State()
    phone = State()
    submit = State()


def generate_random_code(length=4):
    caracteres = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return 'ATM-' + ''.join(random.choice(caracteres) for _ in range(length))



async def start_reg(message: types.Message):
    await message.answer('Введите ФИО: ', reply_markup=buttons.cancel_button)
    await reg.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer('Введите номер телефона:')
    await reg.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

        data['code'] = generate_random_code()

    await reg.next()


    await message.answer(
        text=f'Верные ли данные?\n\n'
             f'Код: {data["code"]}\n'
             f'ФИО: {data["fullname"]}\n'
             f'Ваш номер телефона: {data["phone"]}\n'
             f'Телефон: 15846020707 \n'
             f'Адрес: 广州市白云区石沙路石井工业区一横路2号A3栋709室, Ваш код:{data["code"]}\n',
        reply_markup=buttons.submit_button
    )

    await state.next()

async def submit(message: types.Message, state: FSMContext):
    kb = ReplyKeyboardRemove()
    if message.text == 'Да':
        async with state.proxy() as data:
            code = data['code']
            fullname = data.get('fullname')
            phone = data.get('phone')


            await update_google_sheets(code, fullname, phone)
            await sql_insert_products(code, fullname, phone)

        await message.answer('Отлично, данные сохранены!', reply_markup=kb)
        await state.finish()
    elif message.text == 'Нет':
        await message.answer('Заполнение анкеты отменено.', reply_markup=kb)
        await state.finish()
    else:
        await message.answer('Пожалуйста, выберите "Да" или "Нет".')

async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)


def register_start_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")

    dp.register_message_handler(start_reg, commands=['get_code'])
    dp.register_message_handler(load_fullname, state=reg.fullname)
    dp.register_message_handler(load_phone, state=reg.phone)
    dp.register_message_handler(submit, state=reg.submit)