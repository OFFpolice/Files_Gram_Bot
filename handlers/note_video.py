import uuid
from aiogram import types
from dispatcher import dp, bot
from database import add_file


@dp.message_handler(content_types=types.ContentTypes.VIDEO_NOTE)
async def new_video_note(message: types.Message):
    file_id = message.video_note.file_id
    unique_id = f"c{str(uuid.uuid4().int)[:10]}"
    await add_file(unique_id, file_id, "video_note")

    bot_info = await bot.get_me()
    bot_username = bot_info.username
    link = f"https://t.me/{bot_username}?start={unique_id}"

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(text="🔁 Переслать...", url=f"https://t.me/share/url?url={link}")
    )
    await message.answer_chat_action(
        action="upload_video_note"
    )
    await message.answer_video_note(
        file_id,
        reply_markup=keyboard
    )
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )
