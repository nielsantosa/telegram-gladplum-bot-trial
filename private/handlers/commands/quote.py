from . import CommandHandler, Update, CallbackContext

import requests
import json

def quote_of_the_day(update: Update, context: CallbackContext):
    update.message.reply_text("Please wait while I am texting the quote...")
    quote = get_quote_of_the_day()
    update.message.reply_text(quote)

def quote_random(update: Update, context: CallbackContext):
    update.message.reply_text("Please wait while I am texting the quote...")
    quote = get_quote_random()
    update.message.reply_text(quote)

def get_quote_of_the_day() -> str:
    url = "https://quotes.rest/qod?language=en"
    try:
        response = requests.get(url)
        quotes_res = response.json()
        quote = quotes_res.get("contents", {}).get("quotes")[0]
        quote_author = quote.get("author")
        quote_content = quote.get("quote")

        quote = f"{quote_content} - {quote_author}"
    except:
        return "you are amazing just the way you are :)"
    return quote

def get_quote_random() -> str:
    url = "https://quotes.rest/quote/random?language=en"
    try:
        response = requests.get(url)
        quotes_res = response.json()
        quote = quotes_res.get("contents", {}).get("quotes")[0]
        quote_author = quote.get("author")
        quote_content = quote.get("quote")

        quote = f"{quote_content} - {quote_author}"
    except:
        return "you are amazing just the way you are :)"
    return quote
