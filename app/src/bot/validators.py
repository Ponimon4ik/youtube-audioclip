import re

from pytube import extract

from src.core.settings import MAX_FILE_SIZE
from src.bot import exceptions
from src.constants.validators import LINK_YOUTUBE, LIVE_STREAM


def validate_link(link):
    regex = re.compile(LINK_YOUTUBE)
    results = regex.search(link)
    if not results:
        raise exceptions.InvalidLinkError


def validate_stream(stream):
    stream_size = stream.filesize
    if stream_size > MAX_FILE_SIZE:
        raise exceptions.SizeTooLargeError(stream_size)


def validate_youtube(youtube):
    status, _ = extract.playability_status(youtube.watch_html)
    if status == LIVE_STREAM:
        raise exceptions.LiveStreamError
    if youtube.age_restricted:
        raise exceptions.AgeRestrictedError
