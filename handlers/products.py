from aiogram import types, Router
from aiogram.filters import Command

prod_router = Router()

@prod_router.message(Command("products"))
async def start(message : types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Категории', callback_data="Категории"),
             types.InlineKeyboardButton(text='Весь асортимент', callback_data="Весь асортимент")]
        ]
    )
    await message.answer(f"привет {message.from_user.username}", reply_markup=kb)