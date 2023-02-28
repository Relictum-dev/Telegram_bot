from aiogram.utils import executor
from creation import dp
from handlers import general
from handlers.general import on_start



# perform working bot commands 

general.register_general_handlers(dp)




executor.start_polling(dp, skip_updates=True, on_startup= on_start)