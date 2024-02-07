from aiogram import Router, F, types
from main2 import bot

ban_router = Router()
forbidden_words = ['дурак', 'чорт', 'идиот']

@ban_router.message()
async def check_message(message: types.Message):
    async def check_message(message: types.Message):
        if any(word in message.text.lower() for word in forbidden_words):
            chat_member = await bot.get_chat_member(message.chat.id, message.from_user.id)
            if chat_member.status not in ("administrator", "creator"):
                await message.reply("Вы использовали запрещенные слова. Вы забанены.")
                await bot.kick_chat_member(message.chat.id, message.from_user.id)
            else:
                await message.reply("Внимание! Администратор отправил сообщение с запрещенным словом.")
        else:
            print('')
