"""
Пример использования AioMongoDriver
"""

import asyncio

from loguru import logger

from driver import AioMongoDriver
from config import mongo_settings


async def example():
    driver = AioMongoDriver(**mongo_settings)
    driver.set_collection("users")
    
    if await driver.admin.command("ping"):
        logger.success("Успешное подключение к базе данных")
    else:
        logger.error("Не удалось подключиться к базе данных")
    
    await driver.insert_one()


if __name__ == "__main__":
    asyncio.run(example())
