from aiogram import types, Router, F
from db.database import get_products_by_cat, get_products

pro_router = Router()


@pro_router.callback_query(F.data == 'Категории')
async def products(call: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text='Sportpit', callback_data="sportpit"),
             types.InlineKeyboardButton(text='arsenal', callback_data="arsenal"),
             types.InlineKeyboardButton(text='gym_price', callback_data="gym")]
        ]
    )
    await call.message.answer('что вы хотите посмотреть', reply_markup=kb)


@pro_router.callback_query(F.data == 'sportpit')
async def book(call: types.CallbackQuery):
    pro = get_products_by_cat(1)
    for product in pro:
        await call.message.answer(f'название: {product[1]}\n'
                                  f'цена: {product[2]}')


@pro_router.callback_query(F.data == 'arsenal')
async def comics(call: types.CallbackQuery):
    pro = get_products_by_cat(2)
    for product in pro:
        await call.message.answer(f'название: {product[1]}\n'
                                  f'цена: {product[2]}')


@pro_router.callback_query(F.data == 'gym')
async def manga(call: types.CallbackQuery):
    pro = get_products_by_cat(3)
    for product in pro:
        await call.message.answer(f'название: {product[1]}\n'
                                  f'цена: {product[2]}')


@pro_router.callback_query(F.data == 'Весь асортимент')
async def product(call: types.CallbackQuery):
    pro = get_products()
    for product in pro:
        await call.message.answer(f'название: {product[1]}\n'
                                  f'цена: {product[2]}')