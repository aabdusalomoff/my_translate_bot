import telebot
from googletrans import Translator

TOKEN = "8385301322:AAFM2GMVeEnQBahc2FzT-CL9vSavVaT2Wy4"
bot = telebot.TeleBot(TOKEN)

translator = Translator()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Tarjimon botimga welcome. O'zbekcha yozin tarjima ingliz tilida chiqadi🗽"
    )

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    try:
        translated = translator.translate(message.text, src='uz', dest='en')
        bot.send_message(message.chat.id, f"Tarjima: {translated.text}")
    except Exception as e:
        bot.send_message(message.chat.id, "Error. Try again😏")

print("Bot ishga tushdi..")
bot.polling()


