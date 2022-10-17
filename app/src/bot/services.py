import os
import re

from moviepy.editor import AudioFileClip
from pytube import YouTube

import logger
from src.bot import exceptions
from src.core.settings import BUFFER_SIZE, DOWNLOAD_PATH, MAX_FILE_SIZE


def validate_link(link):
    regex = re.compile(
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    )
    results = regex.search(link)
    if not results:
        raise exceptions.InvalidLinkError


def validate_size_stream(stream):
    stream_size = stream.filesize
    if stream_size > MAX_FILE_SIZE:
        raise exceptions.SizeTooLargeError(stream_size)


def validate_age_restricted(youtube):
    if youtube.age_restricted:
        raise exceptions.AgeRestrictedError


def get_stream(link):
    try:
        validate_link(link)
        youtube = YouTube(link)
        validate_age_restricted(youtube)
        stream = youtube.streams.get_audio_only()
        validate_size_stream(stream)
        stream.download(output_path=DOWNLOAD_PATH)
        return stream
    except (
            exceptions.InvalidLinkError,
            exceptions.AgeRestrictedError,
            exceptions.SizeTooLargeError,
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
