import telepot
import configparser
import time

CONFIG_FILE = '.config'
DEFAULT_CHAT_MESSAGE_TYPE = 'text'
ONLY_TEXT_WARNING = 'Sorry! I can only talk via text... ;('

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

token = config.get('TelegramToken', 'token')

bot = telepot.Bot(token)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type != DEFAULT_CHAT_MESSAGE_TYPE:
        bot.sendMessage(chat_id, ONLY_TEXT_WARNING)
    else:
        message = msg['text']
        bot.sendMessage(chat_id, message)

bot.message_loop(handle)

# Keep the program running.
while 1:
    time.sleep(10)
