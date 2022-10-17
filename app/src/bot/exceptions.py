from src.constants.exceptions import (AGE_RESTRICTED, INVALID_LINK,
                                      SIZE_TOO_LARGE, UNEXPECTED_ERROR)


class Base(Exception):
    """Базовый класс"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class SizeTooLargeError(Base):
    """Вызывается, когда размер файла превышает допустимый"""

    def __init__(self, size, message=SIZE_TOO_LARGE):
        self.size = size
        super().__init__(message)

    def __str__(self):
        return f'{self.size} byte. {self.message}'


class InvalidLinkError(Base):
    """Вызывается, когда пользователь присылает
    неверную ссылку на ютуб видео"""

    def __init__(self, message=INVALID_LINK):
        super().__init__(message)


class AgeRestrictedError(Base):
    """Вызывается, когда пользователь присылает
    ссылку на ютуб видео c ограничением по возрасту"""

    def __init__(self, message=AGE_RESTRICTED):
        super().__init__(message)


class UnexpectedError(Base):
    """Вызывается, когда происходит неожиданная ошибка"""

    def __init__(self, message=UNEXPECTED_ERROR):
        super().__init__(message)
