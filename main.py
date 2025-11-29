from asyncio import run
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
import message

print("Import muvaffaqiyatli")


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    print("Bot va Dispatcher yaratildi")

    dp.include_router(message.router)
    print("Router qo'shildi")

    print("Polling boshlanmoqda...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(main())


