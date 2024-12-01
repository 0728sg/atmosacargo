from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
import os
from buttons import start
from config import bot


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text= 'Здравствуйте!\n\n'
                              'Это бот для генерации уникального кода\n'
                              'Доступные команды:\n'
                              '/get_code  - получение уникального кода\n'
                              '/track  - отслеживание товара')




async def track(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Сервис в разработке 😊.\n'
                                                              'Но можете написать и уточнить у менеджера \n'
                                                              'по номеру телефона +996505480008')



def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(track, commands=['track'])