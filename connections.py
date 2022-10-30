import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5493898156:AAEp-P_kHkR_nkt-ANRendLt43SyyGTG0A8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
