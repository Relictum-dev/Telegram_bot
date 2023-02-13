from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config.hidden import Token


Doctor = Bot(token=Token)
dp = Dispatcher(Doctor)