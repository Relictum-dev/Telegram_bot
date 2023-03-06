from aiogram.utils import executor
from create import dp
from handler import user
from database import sql_start

# Вызов хендреров и базы данных из других файлов
async def connection_sql(_):
    sql_start()

user.register_handlers(dp)







# Беспрерывный поллинг бота 
executor.start_polling(dp, skip_updates=True, on_startup=connection_sql)