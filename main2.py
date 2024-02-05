from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv



load_dotenv()
TOKEN = getenv("TOKEN_BOT")
bot = Bot(token=TOKEN)
dp = Dispatcher()



async def set_commands():
    """
    Настройка команд
     в меню бота
    """
    # строка выше наз-ся Docstring
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Старт"),
    ])