import os
import logging

from dotenv import load_dotenv
from os.path import join, dirname

from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


API_TOKEN = os.environ.get("API_TOKEN")


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)
