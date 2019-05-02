from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def get_url():
    payload = {'api_key': '9doovkt23xwwYE0Ot5RMwLnoI0ssMpfW', 'tag': 'owl'}
    contents = requests.get('https://api.giphy.com/v1/gifs/random', params=payload).json()
    image_url = contents['data']['image_url']
    return image_url


def owl(bot, update):
    bot.sendAnimation(chat_id=update.message.chat_id, animation=get_url())


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    updater = Updater('895599799:AAGGaQgvjVyXiy73iloOOVdb0ZoR2Sbe4EY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('owl', owl))
    dp.add_handler(MessageHandler(Filters.regex('(?i)(совун*)'), owl))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
