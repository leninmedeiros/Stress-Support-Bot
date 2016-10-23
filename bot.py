import telepot
import configparser
import time
import logging
import reasoning
import uuid
from pymongo import MongoClient
import time

CONFIG_FILE = '.config'
DEFAULT_CHAT_MESSAGE_TYPE = 'text'
ONLY_TEXT_WARNING = 'Sorry! I can only talk via text... ;('

SOMETHING_WENT_WRONG_MESSAGE = (
    "Oops! For some reason that I don't know yet I "
    "couldn't understand you this time. ;( "
    "I'm so sorry! I'm working on it in order to "
    "find out what went wrong. "
    "Please try again the same message later, OK? "
    "Now you can try saying it differently if you "
    "want..."
    "I would be very happy in helping you! :D"
)

HINT_MESSAGE = (
    "Just type a message describing a given stressful situation."
    " And please make sure you are not using any especial character like '/'."
)

logging.basicConfig(level=logging.INFO)
logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s]" +
    "[%(levelname)-5.5s]  %(message)s"
    )
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(filename="bot.log")
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

token = config.get('TelegramToken', 'token')
db_name = config.get('DB_Name', 'db')
server = config.get('DB_Server', 'server')
port = config.get('DB_Port', 'port')
username = config.get('DB_Username', 'username')
password = config.get('DB_Password', 'password')

db = MongoClient(host=server, port=int(port))
db[db_name].authenticate(username, password)


bot = telepot.Bot(token)


def handle(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != DEFAULT_CHAT_MESSAGE_TYPE:
            bot.sendMessage(chat_id, ONLY_TEXT_WARNING)
        else:
            if msg['text'][0] == "/":
                bot.sendMessage(chat_id, HINT_MESSAGE)
            else:
                username = msg['from']['username']
                users = db[db_name].users
                user = db[db_name].users.find_one({"username": username})
                user_id = ""

                if user is None:
                    user_id = str(uuid.uuid4())
                    user = {"_id": user_id,
                            "username": username,
                            "usefull": "",
                            "group": "",
                            "time_created": time.asctime(
                                time.localtime(time.time()))}
                    users.insert_one(user)
                else:
                    user_id = user['_id']

                processed_response = reasoning.process_incoming_message(
                    msg['text'], msg['chat']['first_name'])

                bot.sendMessage(chat_id, processed_response['response'])

                messages = db[db_name].messages

                message = {"_id": str(uuid.uuid4()),
                           "user": user_id,
                           "message": msg['text'],
                           "situation": processed_response['situation'],
                           "strategy": processed_response['strategy'],
                           "response": processed_response['response'],
                           "time_created": time.asctime(
                               time.localtime(time.time()))}

                messages.insert_one(message)

    except Exception as e:
        log_msg = 'The message sent by the user was "%s"' % msg['text']
        logging.exception(str(e)+"\n%s" % log_msg)
        bot.sendMessage(chat_id, SOMETHING_WENT_WRONG_MESSAGE)

bot.message_loop(handle)

# Keep the program running.
while 1:
    time.sleep(10)
