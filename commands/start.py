from aiogram import types
from dispatcher import dp, bot
from database import get_file
from commands.help import cmd_help
from commands.privacy import cmd_privacy


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    args = message.get_args()
    if args == "privacy":
        await cmd_privacy(message)
    elif args == "help":
        await cmd_help(message)
    else:
        file_info = await get_file(args)
        if file_info:
            file_id, file_type = file_info

            await message.answer(
                "<b>Отправляю файл...</b>",
                parse_mode="HTML"
            )

            if file_type == "video":
                await message.answer_chat_action(
                    action="upload_video"
                )
                await message.answer_video(file_id)

            elif file_type == "audio":
                await message.answer_chat_action(
                    action="upload_audio"
                )
                await message.answer_audio(file_id)

            elif file_type == "photo":
                await message.answer_chat_action(
                    action="upload_photo"
                )
                await message.answer_photo(file_id)

            elif file_type == "animation":
                await message.answer_chat_action(
                    action="upload_video"
                )
                await message.answer_animation(file_id)

            elif file_type == "document":
                await message.answer_chat_action(
                    action="upload_document"
                )
                await message.answer_document(file_id)

        else:
            bot_info = await bot.get_me()
            bot_username = bot_info.username

            await message.answer(
                f"<b>Файл не найден.</b>\n\n<i>Но вы можете отправить мне свой файл и я сгенерирую для вас ссылку для доступа к вашему файлу.</i>\n\n/privacy — <a href=\'https://t.me/{bot_username}?start=privacy'>Политика конфиденциальности</a>\n/help — <a href=\'https://t.me/{bot_username}?start=help'>Помощь</a>",
                parse_mode="HTML"
            )
