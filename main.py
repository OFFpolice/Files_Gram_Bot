import asyncio

from aiogram import executor, types
from dispatcher import dp, bot
from database import init_db

from commands.start import cmd_start
from commands.help import cmd_help
from commands.privacy import cmd_privacy

from handlers.video import new_video
from handlers.audio import new_audio
from handlers.photo import new_photo
from handlers.animation import new_animation
from handlers.document import new_document


async def register_commands():
    dp.register_message_handler(
        cmd_start,
        commands=["start"]
    )
    dp.register_message_handler(
        cmd_help,
        commands=["help"]
    )
    dp.register_message_handler(
        cmd_privacy,
        commands=["privacy"]
    )


async def register_handlers():
    dp.register_message_handler(
        new_video,
        content_types=types.ContentTypes.VIDEO
    )
    dp.register_message_handler(
        new_audio,
        content_types=types.ContentTypes.AUDIO
    )
    dp.register_message_handler(
        new_photo,
        content_types=types.ContentTypes.PHOTO
    )
    dp.register_message_handler(
        new_animation,
        content_types=types.ContentTypes.ANIMATION
    )
    dp.register_message_handler(
        new_document,
        content_types=types.ContentTypes.DOCUMENT
    )


async def set_commands():
    commands = [
        types.BotCommand(
            command="/start",
            description="🤖 Старт"
        ),
        types.BotCommand(
            command="/help",
            description="⁉️ Помощь"
        ),
        types.BotCommand(
            command="/privacy",
            description="👤 Политика конфиденциальности"
        )
    ]
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init_db())
    loop.run_until_complete(register_commands())
    loop.run_until_complete(register_handlers())
    loop.run_until_complete(set_commands())
    executor.start_polling(dp, skip_updates=True)
