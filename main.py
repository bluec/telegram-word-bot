import logging
from strings import RESPONSE_MSG, HELP_MSG, HELLO_MSG, NOT_WORD_MSG
from word import Word
from config import BOT_TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def hi(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(HELLO_MSG)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text(HELP_MSG)


def analyse(update, context):
    """Analyse the user message."""
    my_word = Word(update.message.text)

    if not my_word.validate():
        update.message.reply_text(NOT_WORD_MSG)
        return

    unique_letters_string = ''
    for key in my_word.unique_letters:
        unique_letters_string += ("%d x %s, " % (my_word.unique_letters[key], key))
    unique_letters_string = unique_letters_string.rstrip(', ')

    if len(my_word.most_frequent_letters) > 1:
        frequent_letters_string = ("letters are %s with %d occurrences each" % (
            ' and '.join(my_word.most_frequent_letters), my_word.most_frequent_letters_count))
    else:
        frequent_letters_string = ("letter is %s with %d occurrences" % (
            ''.join(my_word.most_frequent_letters), my_word.most_frequent_letters_count))

    update.message.reply_text(RESPONSE_MSG.format(my_word.word,
                                                  my_word.length,
                                                  my_word.vowels_count,
                                                  my_word.consonants_count,
                                                  len(my_word.unique_letters),
                                                  unique_letters_string,
                                                  frequent_letters_string
                                                  ))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("hi", hi))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - analyse the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, analyse))

    # log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
