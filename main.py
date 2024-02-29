from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import threading
import time

TOKENS = [
    '6490338625:AAEFDgX1DEPgbaR0vV7YeXgE9S_UB-pSuPw',
    '6879617793:AAG4sSlqFh7uvONgINYAwgMRVakCD2fYMLg',
    '6808434898:AAFJ_gz7dtUmvFKn9f7bJPD-U1MSxy2yeYE',
    '6977634869:AAE93iKkQo3bqOI9Eh5sGd6Lyh876AyIBho',
    '6453739411:AAERpct7HGemprlP0IoUCMEMsGvlaT-IseQ'
]
GROUP_CHAT_ID = -1002023478062  # Replace with your actual group chat ID

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Starting count every 4 seconds...')
    count_bot(GROUP_CHAT_ID)

def count_bot(chat_id):
    count = 1
    while True:
        for token in TOKENS:
            bot = Updater(token).bot
            bot.send_message(chat_id, text=str(count))
            time.sleep(1)  # Adjust this sleep time to control the frequency of messages
        count += 1
        time.sleep(3)  # Adjust this sleep time to control the frequency of batches

if __name__ == '__main__':
    updater = Updater(TOKENS[0])
    updater.dispatcher.add_handler(CommandHandler('start', start))
    threading.Thread(target=updater.start_polling, name='Bot-1').start()

    # Keep the main thread running
    updater.idle()
