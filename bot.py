import telepot
import configparser
import time

CONFIG_FILE = '.config'
config = configparser.ConfigParser()
config.read(CONFIG_FILE)

token = config.get('TelegramToken', 'token')

bot = telepot.Bot(token)


def handle(message):
    print('the message')
    print(message)


bot.message_loop(handle)

# Keep the program running.
while 1:
    time.sleep(10)
