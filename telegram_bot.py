import logging
import time
from threading import Thread
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up basic logging to see what's happening
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# my bot's token from BotFather
TOKEN = "7587114030:AAGRpN489C2OujSwx4whIZU1pLZloJDcox0"

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the /start command is issued."""
    welcome_message = """
    Hello! I'm your automated messaging bot. 
    I can help automate messages in this group.
    Use /help to see what I can do.
    """
    update.message.reply_text(welcome_message)

def help_command(update: Update, context: CallbackContext) -> None:
    """Send a help message when the /help command is issued."""
    help_text = """
    🛠 Available Commands:
    /start - Start the bot
    /help - Show this help message
    /autohello - I'll send an automated greeting
    /schedulepost [message] - Schedule a message (basic example)
    """
    update.message.reply_text(help_text)

def auto_hello(update: Update, context: CallbackContext) -> None:
    """Automatically send a greeting message to the group."""
    greeting = "👋 Hello everyone! This is an automated greeting from your friendly bot!"
    update.message.reply_text(greeting)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message (basic AI response simulation)."""
    user_message = update.message.text
    # Simple "AI" response - in a real bot you'd integrate with an AI API
    ai_response = f"🤖 Bot received: '{user_message}'. This is a simulated response."
    update.message.reply_text(ai_response)

def error_handler(update: Update, context: CallbackContext) -> None:
    """Log errors and notify the user."""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)
    update.message.reply_text("⚠️ An error occurred. Please try again later.")
    
def schedule_post(update: Update, context: CallbackContext) -> None:
    """Scheduling a message to be sent after a custom delay. """
    if not context.args:
        update.message.reply_text("Usage: /schedulepost <message> <delay_seconds>")
        return
    try:
        # Extract message and delay from command arguments
        delay = int(context.args[-1])  # Last argument is the delay
        message_text = " ".join(context.args[:-1])  # All except last are the message

        update.message.reply_text(f" Scheduled: '{message_text}' in {delay} seconds.")

        # Schedule the message (using a simple thread for demonstration)
        def send_delayed_message():
            time.sleep(delay)
            update.message.reply_text(f"📨 Notice: {message_text}")

        Thread(target=send_delayed_message).start()

    except (IndexError, ValueError):
        update.message.reply_text("❌ Invalid format. Use: /schedulepost <message> <delay_seconds>")
    

def main() -> None:
    """Start the bot and set up command handlers."""
    # Create the Updater and pass it your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("autohello", auto_hello))
    dispatcher.add_handler(CommandHandler("schedulepost", schedule_post)) 

    # Register a message handler for regular text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Register error handler
    dispatcher.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()