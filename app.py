from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests
import json


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

with open('config.json', 'r') as temp:
    data = temp.read()
tokens = json.loads(data)


def get_url():
    giphy_token = str(tokens['giphy_token'])
    payload = {'api_key': giphy_token, 'tag': 'owl'}
    contents = requests.get('https://api.giphy.com/v1/gifs/random', params=payload).json()
    image_url = contents['data']['image_url']
    return image_url


def owl(bot, update):
    bot.sendAnimation(chat_id=update.message.chat_id,
                      animation=get_url(),
                      reply_to_message_id=update.message.message_id)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def jopa_someone(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="какой же Коля гомосек",
                    reply_to_message_id=update.message.message_id)

def jopa(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="какой же ты гомосек",
                    reply_to_message_id=update.message.message_id)

def main():
    telegram_token = str(tokens['telegram_token'])
    updater = Updater(telegram_token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('owl', owl))
    dp.add_handler(MessageHandler(Filters.regex('(?i)(совун*)|\U0001F989'), owl))
    dp.add_handler(MessageHandler(Filters.user(user_id=53303105) & Filters.regex('(?i)(жопа*)|(?i)(срака*)'), jopa))
    dp.add_handler(MessageHandler(Filters.regex('(?i)(жопа*)|(?i)(срака*)'), jopa_someone))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
