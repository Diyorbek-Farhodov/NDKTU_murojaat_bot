from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from .states import Form


async def admin_message(message: Message):
    if message.reply_to_message:
        if message.reply_to_message.forward_from:
            chat_id = message.reply_to_message.forward_from.id
            await message.copy_to(chat_id=chat_id)
            await message.answer("✅ Sizning xabaringiz foydalanuvchiga yuborildi")
        else:
            await message.answer(
                "❗ Bu xabar boshqa foydalanuvchidan oldinga yuborilmagan."
            )
    else:
        await message.answer(
            "❗ Kimgadur xabar yozmoqchi bo'lsangiz, reply qilib yuboring"
        )


async def admin_callback(call: CallbackQuery, state: FSMContext):
    user_id = call.data.split("_")[1]

    await state.update_data(chat_id=user_id)
    await call.message.answer("Javob xabarini yozing:")
    await state.set_state(Form.get_admin_message)

    await call.answer()


async def get_admin_message(message: Message, state: FSMContext):
    data = await state.get_data()
    chat_id = data.get("chat_id")

    try:
        await message.bot.send_message(
            chat_id=int(chat_id),
            text=f"📨 Admin javobi:\n\n{message.text}"
        )

        await message.answer("✅ Sizning xabaringiz foydalanuvchiga yuborildi")

        await state.clear()

    except Exception as e:
        await message.answer(f"❌ Xabar yuborishda xato: {e}")
        await state.clear()