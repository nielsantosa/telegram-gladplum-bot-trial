#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import os
from dotenv import load_dotenv

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from private.handlers import (
    commands,
    messages
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

class WebApplication(object):
    def __init__(self, config):
        # Create the Updater and pass it your bot's token.
        self.updater = Updater(token=config.get("token"))
        # Get the dispatcher to register handlers
        self.dispatcher = self.updater.dispatcher

    def set_bindings(self):
        # Declare bindings (handlers)
        bindings = []
        bindings.extend(commands.BINDINGS)
        bindings.extend(messages.BINDINGS)

        return bindings

    def set_handlers(self):
        bindings = self.set_bindings()
        # Adding handlers to the dispatcher
        # Define a few command handlers. These usually take the two arguments update and
        # context.
        for binding in bindings:
            self.dispatcher.add_handler(binding)

    def run(self):
        # Start the Bot
        self.updater.start_polling()
        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()

def load_environment() -> None:
    load_dotenv()
    global BOT_TOKEN
    BOT_TOKEN = os.environ.get("BOT_TOKEN")

def main() -> None:
    # load env
    load_environment()
    # set config
    config = {
        "token": BOT_TOKEN
    }

    """Start the bot."""
    app = WebApplication(config)

    # Declare bindings
    app.set_bindings()

    # Set handlers
    app.set_handlers()

    # Start the Bot
    app.run()


if __name__ == '__main__':
    main()
