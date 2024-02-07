import asyncio
import logging
from main2 import bot, dp, set_commands
from handlers.start import start_router
from handlers.info import info_router
from db.database import init_db, create_tables
from handlers.prod import pro_router
from handlers.products import prod_router
from parser.houses import parser_router
from handlers.schedule import scheduler_router, scheduler
from handlers.ban_in_group import ban_router

# from handlers.pic import pic_router
# from handlers.opros import opros_router

logging.basicConfig(level=logging.INFO)
async def on_startapp():
    init_db()
    create_tables()
    # fill_db()
    print('база данных подключена')


async def main():
    (dp.include_router(start_router),
     dp.include_router(info_router),
     dp.include_router(prod_router),
     dp.include_router(pro_router),
     dp.startup.register(on_startapp),
     dp.include_router(parser_router),
     dp.include_router(scheduler_router),
     dp.include_router(ban_router),
     scheduler.start(),



     # dp.include_router(pic_router),
     # dp.include_router(opros_router),
     await dp.start_polling(bot))


if __name__ == '__main__':
    asyncio.run(main())