from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# TOKEN = config('TOKEN')
TOKEN = "7869540023:AAEqgxIATsKEJ50lu4eJBsQDVeJ52zM-3ag"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

admin = [371110883, ]