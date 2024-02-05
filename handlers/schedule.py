from aiogram import Router, F, types
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from main2 import bot


scheduler_router = Router()
scheduler = AsyncIOScheduler()


@scheduler_router.message(F.text.startswith("напомни"))
async def process_notify(message: types.Message):
    scheduler.add_job(
        send_notification,
        "interval",
        seconds=5,
        kwargs={"chat_id": message.from_user.id,
                'text': message.text.replace('напомни ', "")}
        )
    await message.answer("Напоминание добавлено")


async def send_notification(chat_id, text):
    await bot.send_message(
        chat_id=chat_id,
        text=text
    )

