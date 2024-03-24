import asyncio
from aiogram import Bot, Dispatcher
from handlers import user_handlers, other_handlers

from config_data.config import Config, load_config

# Функция конфигурирования и запуска бота
async def main() -> None:
    
    config: Config = load_config()
    
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
   
    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())
    