from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config.settings import Token
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# сreation CPU memory storage
storage = MemoryStorage()

# creation copy tg bot
Doctor = Bot(token=Token)
dp = Dispatcher(Doctor, storage=storage)