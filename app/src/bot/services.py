import os

from moviepy.editor import AudioFileClip
from pytube import YouTube

from src.bot.exceptions import InvalidLinkError, SizeTooLargeError
from src.core.settings import BUFFER_SIZE, DOWNLOAD_PATH, MAX_FILE_SIZE


def validate_size_stream(stream):
    stream_size = stream.filesize
    if stream_size > MAX_FILE_SIZE:
        raise SizeTooLargeError(stream_size)


def get_stream(link):
    try:
        stream = YouTube(link).streams.get_audio_only()
        validate_size_stream(stream)
        stream.download(output_path=DOWNLOAD_PATH)
        return stream
    except SizeTooLargeError as mistake:
        raise mistake
    except Exception:
        raise InvalidLinkError


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
