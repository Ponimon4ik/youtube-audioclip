from src.main import create_bot
import logger

if __name__ == '__main__':
    logger.bot_started()
    create_bot().run_polling()
