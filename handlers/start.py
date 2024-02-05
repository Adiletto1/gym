from aiogram import Router, F, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='О магазине',
                                           callback_data='about_us'),
                types.InlineKeyboardButton(text='О нас',
                                           callback_data='О нас')
            ],
            [
                types.InlineKeyboardButton(text='Каталог товаров',
                                           callback_data='О спортпите'),
                types.InlineKeyboardButton(text="Houses", callback_data="house")
            ]
        ]
    )
    await message.answer(text='Привет', reply_markup=kb)


@start_router.callback_query(F.data == 'about_us')
async def about_us(callback: types.CallbackQuery):
    await callback.message.answer(
        'На сегодняшний день уже никто не сомневается в том, что спортивное питание является одним из главных компонентов для достижения спортивных результатов. Ежедневно в мире спорта проводятся разработки и многочисленные испытания новейших добавок, которые необходимы профессиональным атлетам и любителям для того, чтобы добиться своих целей – построить красивое тело и укрепить здоровье. Существует огромное множество спортивных добавок, но в целом, они преследуют общие цели – увеличение мышечной массы, похудение и сжигание подкожного жира, укрепление здоровья и поддержка организма.')


@start_router.callback_query(F.data == 'О нас')
async def avtor(callb: types.CallbackQuery):
    await callb.message.answer('Это сектетная информация!')


@start_router.callback_query(F.data == 'О спортпите')
async def fight_list(call: types.CallbackQuery):
    sb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Протеин'),
                types.KeyboardButton(text='Гейнер')
            ],
            [
                types.KeyboardButton(text='Креатин'),
                types.KeyboardButton(text='BCAA')
            ]
        ], resize_keyboard=True

    )
    await call.message.answer('Выберите товар:', reply_markup=sb)


@start_router.message(F.text == 'Протеин')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    photo = types.FSInputFile('images/d968bd2d139bb996567d88fbe93fb99e.jpg')
    await message.answer_photo(photo=photo, caption='Протеин это батя среди спортивного питания!')


@start_router.message(F.text == 'Гейнер')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    photo = types.FSInputFile('images/1bf9900674f4f5b9ce4a4740b57fb56f.jpg')
    await message.answer_photo(photo=photo, caption='Стоит так же дорого как и протеин, но в нем еще содержится много углеводов')


@start_router.message(F.text == 'Креатин')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    photo = types.FSInputFile('images/3fec0b353d28893a1cc7122569d79b93.jpg')
    await message.answer_photo(photo=photo, caption='А этот ништяк даст тебе больше выносливости и силы!')


@start_router.message(F.text == 'BCAA')
async def first(message: types.Message):
    sb = types.ReplyKeyboardMarkup
    photo = types.FSInputFile('images/380cf5321275c9e72a123e2609438d71.jpg')
    await message.answer_photo(photo=photo, caption='Три богатыря стоят на стражи твоего миафибрильного царства и именуются они как BCAA')

