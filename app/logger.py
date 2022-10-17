import logging


LOG_BOT_STARTED = 'Бот запущен'
LOG_BOT_PROBLEMS = 'При работе Бота возникла ошибка: {mistake}'
LOG_SENT_MESSAGE = 'Отправлено сообщение: "{message}"'
LOG_SENT_AUDIO_FILE = 'Отправлено аудио файл: "{file_name}"'
LOG_GOT_LINK = 'Получена ссылка: "{link}"'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def bot_started():
    logger.debug(LOG_BOT_STARTED)


def bot_problems(mistake):
    logger.exception(
        LOG_BOT_PROBLEMS.format(mistake=mistake)
    )


def bot_sent_message(message):
    logger.info(
        LOG_SENT_MESSAGE.format(message=message),
    )


def bot_got_link(link):
    logger.info(
        LOG_GOT_LINK.format(link=link)
    )


def bot_sent_audio_file(file_name):
    logger.info(
        LOG_SENT_AUDIO_FILE.format(file_name=file_name)
    )
