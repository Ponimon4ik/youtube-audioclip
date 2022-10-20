from telegram.ext import CallbackContext

import logger
from src.bot import exceptions
from src.bot.services import (convert_mp4_to_mp3, get_stream,
                              remove_mp4_and_mp3_file)
from src.core.settings import WRITE_TIMEOUT


async def job_send_audio(context: CallbackContext):
    data = context.job.data
    link, username = data['link'], data['username']
    logger.bot_got_link(link, username)
    try:
        stream = get_stream(link)
        name_file = stream.default_filename.split('.mp4')[0]
        mp3_file = convert_mp4_to_mp3(name_file)
        await context.bot.send_audio(
            chat_id=context.job.chat_id,
            audio=open(mp3_file, 'rb'),
            write_timeout=WRITE_TIMEOUT
        )
        logger.bot_sent_audio_file(name_file, username)
        remove_mp4_and_mp3_file(name_file)
    except (
            exceptions.InvalidLinkError,
            exceptions.SizeTooLargeError,
            exceptions.AgeRestrictedError,
            exceptions.UnexpectedError,
            exceptions.LiveStreamError
    ) as mistake:
        message = mistake.message
        await context.bot.send_message(
            chat_id=context.job.chat_id,
            text=message
        )
        logger.bot_sent_message(message, username)
