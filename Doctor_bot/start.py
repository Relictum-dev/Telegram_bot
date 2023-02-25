from aiogram.utils import executor
from creation import dp

from handlers import client,admin,general
from database.register import connected_db

async def starting_bot():
    connected_db()
    general.register_general_handlers(dp)
    



executor.start_polling(dp, skip_updates=True)