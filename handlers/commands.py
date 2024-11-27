from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os
from buttons import start
from config import bot


async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text= 'Здравствуйте!\n\n'
                              'Это бот для генерации уникального кода\n'
                              'Доступные команды:\n'
                              '/registration  - получение уникального кода\n'
                              '/track  - отслеживание товара')
    await message.answer()




async def start_reg(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Начните регистрацию')
    await message.answer(text='Начните регистрацию')




async def track(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Введите ваш код')
    await message.answer(text='Введите ваш код')


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(start_reg, commands=['start_reg'])
    dp.register_message_handler(track, commands=['track'])
