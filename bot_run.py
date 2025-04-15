from loguru import logger
import asyncio

from create_bot import bot, dp



async def main():
    logger.add("loging.log", colorize=True, format="<green>{time}</green> <level>{message}</level>")
    logger.info('ЗАПУСК БОТА!')

    # dp.include_router(main_menu)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        logger.info('ОСТАНОВКА РАБОТЫ БОТА!')