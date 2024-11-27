from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import buttons
from google_sheets.sheets import update_google_sheets
import random


class FSM_reg(StatesGroup):
    code = State()
    fullname = State()
    phone = State()
    submit = State()


# Function to generate a random code
def generate_random_code(length=6):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    return ''.join(random.choice(caracteres) for _ in range(length))


async def start_reg(message: types.Message):
    await message.answer('Введите ФИО: ', reply_markup=buttons.cancel_button)
    await FSM_reg.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer('Введите номер телефона:')
    await FSM_reg.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        # Generate and store the code
        data['code'] = generate_random_code()

    await FSM_reg.next()

    # Send confirmation message with generated code
    await message.answer(
        text=f'Верные ли данные?\n\n'
             f'Код: {data["code"]}\n'
             f'ФИО: {data["fullname"]}\n'
             f'Номер телефона: {data["phone"]}\n',
        reply_markup=buttons.submit_button
    )

    await FSM_reg.next()


async def submit(message: types.Message, state: FSMContext, db_main_sql_insert_products=None):
    kb = ReplyKeyboardRemove()
    if message.text == 'Да':
        await message.answer('Отлично, данные в базе!', reply_markup=kb)
        async with state.proxy() as data:
            await update_google_sheets(data)
        await state.finish()

    elif message.text == 'Нет':
        await message.answer('Хорошо, заполнение анкеты завершено!', reply_markup=kb)
        await state.finish()

    else:
        await message.answer('Выберите "Да" или "Нет"')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()

    kb = ReplyKeyboardRemove()

    if current_state is not None:
        await state.finish()
        await message.answer('Отменено!', reply_markup=kb)


def register_start_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")

    dp.register_message_handler(start_reg, commands=['registration'])
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)
    dp.register_message_handler(submit, state=FSM_reg.submit)
