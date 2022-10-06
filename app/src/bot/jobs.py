from telegram.ext import CallbackContext

from src.bot.exceptions import InvalidLinkError, SizeTooLargeError
from src.bot.services import (convert_mp4_to_mp3, get_stream,
                              remove_mp4_and_mp3_file)
from src.core.settings import WRITE_TIMEOUT


async def job_send_audio(context: CallbackContext):
    try:
        stream = get_stream(context.job.data)
        name_file = stream.default_filename.split('.mp4')[0]
        mp3_file = convert_mp4_to_mp3(name_file)
        await context.bot.send_audio(
            chat_id=context.job.chat_id,
            audio=open(mp3_file, 'rb'),
            write_timeout=WRITE_TIMEOUT
        )
        remove_mp4_and_mp3_file(name_file)
    except InvalidLinkError as mistake:
        await context.bot.send_message(
            chat_id=context.job.chat_id,
            text=mistake.message
        )
    except SizeTooLargeError as mistake:
        await context.bot.send_message(
            chat_id=context.job.chat_id,
            text=mistake.message
        )
