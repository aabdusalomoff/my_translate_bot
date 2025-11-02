import telebot
from googletrans import Translator
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
translator = Translator()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "🤖 Tarjimon botga xush kelibsiz!\n\n"
        "O'zbekcha yozing — ingliz tiliga tarjima qilaman\n"
        "Inglizcha yozing — o'zbek tiliga tarjima qilaman"
    )

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    try:
        text = message.text.strip()
        
        if len(text) > 4000:
            bot.send_message(message.chat.id, "⚠️ Matn juda uzun. 4000 belgidan kamroq yuboring.")
            return
        
        # Inglizcha matnni tekshirish
        if any(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' for char in text):
            # Inglizcha -> O'zbekcha
            translated = translator.translate(text, src='en', dest='uz')
            response = f"🇬🇧 EN → 🇺🇿 UZ\n\n{translated.text}"
        else:
            # O'zbekcha -> Inglizcha
            translated = translator.translate(text, src='uz', dest='en')
            response = f"🇺🇿 UZ → 🇬🇧 EN\n\n{translated.text}"
        
        bot.send_message(message.chat.id, response)
        
    except Exception as e:
        bot.send_message(message.chat.id, "⚠️ Xato yuz berdi. Qayta urinib ko'ring.")

if __name__ == "__main__":
    print("✅ Bot ishga tushdi...")
    bot.polling(none_stop=True)