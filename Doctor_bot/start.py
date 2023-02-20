from aiogram.utils import executor
from creation import dp

from handlers import client,admin


client.register_client_handlers(dp)

executor.start_polling(dp, skip_updates=True)