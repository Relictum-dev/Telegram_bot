from aiogram import Bot
from aiogram.dispatcher import Dispatcher

from config.settings import Token


Doctor = Bot(token=Token)
dp = Dispatcher(Doctor)