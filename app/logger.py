import logging

LOG_BOT_STARTED = 'Бот запущен'
LOG_BOT_PROBLEMS = 'При работе Бота возникла ошибка: {mistake}'
LOG_SENT_MESSAGE = 'Пользователю {user} отправлено сообщение: "{message}"'
LOG_SENT_AUDIO_FILE = 'Пользователю {user} отправлен аудио файл: "{file_name}"'
LOG_GOT_LINK = 'От пользователя {user} получена ссылка: "{link}"'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())


def bot_started():
    logger.debug(LOG_BOT_STARTED)


def bot_problems(mistake):
    logger.exception(
        LOG_BOT_PROBLEMS.format(mistake=mistake)
    )


def bot_sent_message(message, user):
    logger.info(
        LOG_SENT_MESSAGE.format(
            user=user,
            message=message
        ),
    )


def bot_got_link(link, user):
    logger.info(
        LOG_GOT_LINK.format(
            user=user,
            link=link
        )
    )


def bot_sent_audio_file(file_name, user):
    logger.info(
        LOG_SENT_AUDIO_FILE.format(
            user=user,
            file_name=file_name
        )
    )
