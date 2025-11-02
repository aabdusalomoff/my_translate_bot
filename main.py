import telebot
from googletrans import Translator
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("❌ TELEGRAM_BOT_TOKEN не найден в .env")

bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "Tarjimon botimga xush kelibsiz! 🇺🇿\n"
        "O'zbekcha yozing — tarjima ingliz tilida chiqadi 🗽"
    )

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    try:
        translated = translator.translate(message.text, src='uz', dest='en')
        bot.send_message(message.chat.id, f"🔤 Tarjima: {translated.text}")
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Xato yuz berdi. Qayta urinib ko‘ring.")

print("✅ Bot ishga tushdi...")
bot.polling(none_stop=True)
