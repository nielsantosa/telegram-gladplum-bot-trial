from . import CommandHandler, Update, CallbackContext

def help_command(update: Update, context: CallbackContext):
    text = (
        "This is a trial bot created by @gladplum.\n"
        "You can control me by sending these commands:\n"
        "\n"
        "/start - will type your name\n"
        "/help - list down all the commands\n"
        "/quote_of_the_day - retrieve quote of the day\n"
        "/quote_random - retrieve a random quote\n"
        "\n"
        "You can also say *hi* or *how are you* to me"
    )
    update.message.reply_text(text)
