import asyncio
from aiogram import Bot, Dispatcher

from config.settings import config
from handlers import commands_handler, callbacks_handler
from utils.logger import logger


async def on_startup(dispatcher: Dispatcher):
    logger.info("Bot was started!")


async def on_shutdown(dispatcher: Dispatcher):
    logger.info("Bot was turned off...")


async def main():
    bot = Bot(token=config.TG_BOT_TOKEN)
    dp = Dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    dp.include_routers(
        commands_handler.router,
        callbacks_handler.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot running was interrupted from console.")
