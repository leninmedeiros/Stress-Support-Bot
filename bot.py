import telepot
import configparser
import time
import logging
import reasoning
import uuid
from pymongo import MongoClient


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

clientDB = MongoClient()


def get_db_name():
    return db_name

bot = telepot.Bot(token)


def handle(msg):
    try:
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type != DEFAULT_CHAT_MESSAGE_TYPE:
            bot.sendMessage(chat_id, ONLY_TEXT_WARNING)
        else:
            id = uuid.uuid4()
            msg_id = "*THANK YOU FOR PARTICIPATING! YOUR ID IS: "+str(id)+"*"

            processed_response = reasoning.process_incoming_message(
                msg['text'], msg['chat']['first_name'])

            bot.sendMessage(chat_id, processed_response['response'])
            bot.sendMessage(chat_id, msg_id, "Markdown")

            db = clientDB[db_name]
            participants_data = db.participants_data

            participant_data = {"_id": str(id),
                                "message": msg['text'],
                                "situation": processed_response['situation'],
                                "strategy": processed_response['strategy'],
                                "response": processed_response['response']}

            participants_data.insert_one(participant_data)
    except Exception as e:
        log_msg = 'The message sent by the user was "%s"' % msg['text']
        logging.exception(str(e)+"\n%s" % log_msg)
        bot.sendMessage(chat_id, SOMETHING_WENT_WRONG_MESSAGE)

bot.message_loop(handle)

# Keep the program running.
while 1:
    time.sleep(10)
