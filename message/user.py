from aiogram import types, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import CHAT_ID


async def command_start_answer(message: types.Message):
    """Start komandasi javob berish"""
    try:
        print(f"Start komandasi keldi: {message.from_user.username}")
        await message.answer(
            "🤖 Navoiy Davlat Konchilik va Texnologiyalar universiteti Yoshlar bilan ishlash, ma'naviyat va ma'rifat bo'lim boshlig'i Jasur Ro'ziyevga Tyutorlar faoliyati bo'yicha murojaatingiz bo'lsa botimizga yozib qoldiring !\n\n"

        )
    except Exception as e:
        print(f"Start komandasi xatosi: {e}")


async def echo(message: types.Message):
    """User xabarlarini admin ga yuborish"""
    try:
        print(f"User xabari: {message.text}")
        print(f"User ID: {message.from_user.id}")
        print(f"Admin CHAT_ID: {CHAT_ID}")

        if message.from_user.id == CHAT_ID:
            return

        user_info = f"👤 {message.from_user.full_name}"
        if message.from_user.username:
            user_info += f" (@{message.from_user.username})"
        user_info += f"\n🆔 ID: {message.from_user.id}"
        user_info += f"\n📝 Xabar: {message.text}"

        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                text="💬 Javob berish",
                callback_data=f"suser_{message.from_user.id}"
            )]
        ])

        bot = message.bot
        await bot.send_message(
            chat_id=CHAT_ID,
            text=f"📨 Yangi xabar keldi:\n\n{user_info}",
            reply_markup=keyboard
        )

        await message.answer("✅ Xabaringiz yuborildi! Tez orada javob beramiz.")

    except Exception as e:
        print(f"Echo xatosi: {e}")
        await message.answer("❌ Xabar yuborishda xato yuz berdi.")