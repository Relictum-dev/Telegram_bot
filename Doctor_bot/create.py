from aiogram import Bot,Dispatcher
from config.settings import Token
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()
Doctor = Bot(token=Token)
dp = Dispatcher(Doctor, storage=storage)