import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# Path settings
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR.joinpath('.env')
DOWNLOAD_PATH = BASE_DIR.joinpath('download')

load_dotenv(dotenv_path=ENV_PATH)

# BOT settings
BOT_TOKEN = os.getenv('TELEGRAM_TOKEN')
BUFFER_SIZE = 5000
MAX_FILE_SIZE = 10*1024*1024  # Максимальный допустимый размер в байтах для mp4
WRITE_TIMEOUT = 60  # Время доступное боту на отправку аудио файла
