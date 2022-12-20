import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a function that will be called whenever a new user joins the group or channel
def welcome(update, context):
    # Get the username of the new user
    username = update.message.new_chat_members[0].username

    # Send a welcome message to the new user
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to the group, @{}!".format(username))

def main():
    # Create the Updater and pass it your bot's token
    updater = Updater("5547968339:AAEEVtwHfTyOgu0bH4utggJFcQY3ue1Oo_A", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add a handler that will be called whenever a new user joins the group or channel
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
