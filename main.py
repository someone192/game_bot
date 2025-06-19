import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import load_config, Config
from handlers import router



async def main():
    # Включаем логирование
    logging.basicConfig(level=logging.INFO)
    
    config: Config = load_config()

    # Инициализируем бота и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    
    # Подключаем роутер с хендлерами
    dp.include_router(router)
    
    # Удаляем все обновления, которые произошли после последнего выключения бота
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main()) 