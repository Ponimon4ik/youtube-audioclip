from src.constants.exceptions import INVALID_LINK, SIZE_TOO_LARGE


class SizeTooLargeError(Exception):
    """Вызывается, когда размер файла превышает допустимый"""

    def __init__(self, size, message=SIZE_TOO_LARGE):
        self.size = size
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.size} byte. {self.message}'


class InvalidLinkError(Exception):
    """Вызывается, когда пользователь присылает
    неверную ссылку на ютуб видео"""

    def __init__(self, message=INVALID_LINK):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
