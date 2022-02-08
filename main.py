import logging
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
    update.message.reply_text('Hi, welcome to the word analysis tool. I think you\'ll like it.')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def analyse(update, context):
    """Analyse the user message."""
    my_word = Word(update.message.text)

    if not my_word.validate():
        update.message.reply_text("That isn't a word.")
        return

    string = ''
    for key in my_word.unique_letters:
        string += ("%d x %s, " % (my_word.unique_letters[key], key))
    string = string.rstrip(', ') + '.'

    update.message.reply_text("Nice word, I like it.")
    update.message.reply_text("\"%s\" is %d letters long." % (my_word.word, my_word.length))
    update.message.reply_text("It has %d vowels and %d consonants." % (my_word.vowels_count, my_word.consonants_count))
    update.message.reply_text("It contains %d unique letters: %s " % (len(my_word.unique_letters), string))

    if len(my_word.most_frequent_letters) > 1:
        update.message.reply_text("The most frequent letters are %s with %d occurrences each." % (
            ' and '.join(my_word.most_frequent_letters), my_word.most_frequent_letters_count))
    else:
        update.message.reply_text("The most frequent letter is %s with %d occurrences." % (
            ''.join(my_word.most_frequent_letters), my_word.most_frequent_letters_count))


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