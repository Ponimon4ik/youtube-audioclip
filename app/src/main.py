from telegram.ext import (ApplicationBuilder, CommandHandler, MessageHandler,
                          filters)

from src.bot.handlers import get_link, start
from src.constants.commands import START
from src.core.settings import BOT_TOKEN


def create_bot():
    """Создать бота"""

    bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
    start_handler = CommandHandler(START, start)
    get_audio_handler = MessageHandler(filters.TEXT, get_link)
    bot_app.add_handlers(
        handlers=[start_handler, get_audio_handler]
    )
    return bot_app
