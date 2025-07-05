import os
from dotenv import load_dotenv
import telebot

load_dotenv()

TOKEN = os.environ.get("7527524095:AAFWxOP12W18r3-XEPVqr7ZAlpmwkBHSmVM")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Salam! Bot .env ilə işləyir ✅")

bot.polling()
