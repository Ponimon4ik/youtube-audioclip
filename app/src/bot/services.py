import os

from moviepy.editor import AudioFileClip
from pytube import YouTube

import logger
from src.bot import exceptions
from src.bot import validators
from src.core.settings import BUFFER_SIZE, DOWNLOAD_PATH


def get_stream(link):
    try:
        validators.validate_link(link)
        youtube = YouTube(link)
        validators.validate_youtube(youtube)
        stream = youtube.streams.get_audio_only()
        validators.validate_stream(stream)
        stream.download(output_path=DOWNLOAD_PATH)
        return stream
    except (
            exceptions.InvalidLinkError,
            exceptions.AgeRestrictedError,
            exceptions.SizeTooLargeError,
            exceptions.LiveStreamError
    ) as mistake:
        raise mistake
    except Exception as mistake:
        logger.bot_problems(mistake)
        raise exceptions.UnexpectedError


def convert_mp4_to_mp3(mp4_file_name):
    audio = AudioFileClip(
        os.path.join(DOWNLOAD_PATH, f'{mp4_file_name}.mp4'))
    path_mp3 = os.path.join(DOWNLOAD_PATH, f'{mp4_file_name}.mp3')
    audio.write_audiofile(path_mp3, buffersize=BUFFER_SIZE)
    audio.close()
    return path_mp3


def remove_mp4_and_mp3_file(name_file, types=('mp4', 'mp3')):
    for type_file in types:
        os.remove(
            os.path.join(DOWNLOAD_PATH, f'{name_file}.{type_file}')
        )
