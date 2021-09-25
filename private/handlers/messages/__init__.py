from .. import *
import re

def base_reply(update: Update, context: CallbackContext) -> None:
    text = (
        "I cannot reply you properly currently for now.\n"
        "Please type /help for the commands that you can give me."
    )

    message_text = update.message.text

    if "hello" in message_text.lower():
        update.message.reply_text(reply_hello())
        return
    elif "how are you" in message_text.lower():
        update.message.reply_text(reply_how_are_you())
        return

    update.message.reply_text(text)

# Non handler function
def reply_hello():
    text = (
        "Hi!"
    )
    return text

def reply_how_are_you():
    text = (
        "I'm good. How about you"
    )
    return text

BINDINGS = [
    #-----------------echo-----------------#
    MessageHandler(Filters.text & ~Filters.command, base_reply),
]
