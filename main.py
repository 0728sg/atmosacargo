import logging

from aiogram import types
from aiogram.utils import executor
from buttons import start_test
from config import bot, dp, admin
from db import db_main
from handlers import commands, echo, start_reg, track
from google_sheets import sheets


async def send_info(message: types.Message):
    text = ("Здравствуйте, я Атмоскарго бот!\n"
            " Я помогу вам получить код"
    )

    await message.answer(text)

commands.register_commands(dp)
track.register_track(dp)
start_reg.register_start_reg(dp)


# echo.register_echo(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)