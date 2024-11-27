from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import buttons
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
import buttons
from google_sheets.sheets import update_google_sheets
import random


class FSM_reg(StatesGroup):
    fullname = State()
    date = State()
    email = State()
    submit = State()


async def start_reg(message: types.Message):
    await message.answer('Введите фио: ', reply_markup=buttons.cancel_button)
    await FSM_reg.fullname.set()


async def load_fullname(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['fullname'] = message.text

    await message.answer('Введите номер телефона:')
    await FSM_reg.next()


async def load_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    await message.answer(
                        caption=f'Верные ли данные?\n\n'
                                f'ФИО: {data["fullname"]}\n'
                                f'Номер телефона: {data["phone"]}\n',
                        reply_markup=buttons.submit_button)

    await FSM_reg.next()


async def generate_code(message: types.Message, state: FSMContext):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        nitrocode = ''

        for i in range(16):
            nitrocode = f"{nitrocode}{random.choice(caracteres)}"

        print({nitrocode})



async def submit(message: types.Message, state: FSMContext, db_main_sql_insert_products=None):
    kb = ReplyKeyboardRemove()
    async with state.proxy() as data:
        await db_main_sql_insert_products(
            code = data['code'],
            name = data['fullname'],
            phone = data['phone']
        )

        code = data['code']
        name = data['fullname']
        phone = data['phone']

        update_google_sheets(code=code,
                             name=name,
                             phone=phone)
    if message.text == 'Да':
        await message.answer('Отлично, Данные в базе!', reply_markup=kb)
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


def register_fsm_reg(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена', ignore_case=True), state="*")

    dp.register_message_handler(start_reg, commands=['reg'])
    dp.register_message_handler(load_fullname, state=FSM_reg.fullname)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)
    dp.register_message_handler(submit, state=FSM_reg.submit)