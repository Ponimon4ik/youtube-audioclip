import logger
from src.main import create_bot

if __name__ == '__main__':
    logger.bot_started()
    create_bot().run_polling()
