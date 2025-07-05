import os
import telebot

TOKEN = os.environ.get("7527524095:AAFWxOP12W18r3-XEPVqr7ZAlpmwkBHSmVM")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Salam! Bot PythonAnywhere-dən işləyir 🟢")

bot.polling()
