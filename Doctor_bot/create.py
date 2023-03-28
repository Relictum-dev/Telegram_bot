from aiogram import Bot,Dispatcher
from config.settings import Token, OWM_Token
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pyowm import OWM

storage = MemoryStorage()
Doctor = Bot(token=Token)
dp = Dispatcher(Doctor, storage=storage)

owm = OWM(OWM_Token)
mrg = owm.weather_manager()