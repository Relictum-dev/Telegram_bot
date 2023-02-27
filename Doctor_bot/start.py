from aiogram.utils import executor
from creation import dp

from handlers import client,admin,general
from database.create_db import Database

async def starting_bot():
    Database()
    general.register_general_handlers(dp)
    



executor.start_polling(dp, skip_updates=True)