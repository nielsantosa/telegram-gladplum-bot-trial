from .. import *

from . import (
    help,
    start,
    quote,
)

BINDINGS = [
    #-----------------start-----------------#
    CommandHandler("start", start.start),
    #-----------------help-----------------#
    CommandHandler("help", help.help_command),
    #-----------------quote-----------------#
    CommandHandler("quote_of_the_day", quote.quote_of_the_day),
    CommandHandler("quote_random", quote.quote_random),
]
