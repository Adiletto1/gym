from aiogram import Router, types
from aiogram.filters import Command

info_router = Router()


@info_router.message(Command("info"))
async def start(message: types.Message):
    await message.answer(f'Твое имя: {message.from_user.username}\nТвой id: {message.from_user.id}\nТвое полное имя: {message.from_user.full_name}')
