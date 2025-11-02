import telebot
from deep_translator import GoogleTranslator
from dotenv import load_dotenv
import os

# .env faylidan o'zgaruvchilarni yuklash
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id,
        "🤖 Tarjimon botga xush kelibsiz!\n\n"
        "Yozing — men avtomatik ravishda tarjima qilaman 🌍\n\n"
        "Masalan:\n"
        "• Hello → Salom\n"
        "• Qandaysiz? → How are you?"
    )

@bot.message_handler(func=lambda message: True)
def translate_text(message):
    try:
        text = message.text.strip()
        if not text:
            bot.send_message(message.chat.id, "⚠️ Iltimos, matn kiriting.")
            return
        if len(text) > 4000:
            bot.send_message(message.chat.id, "⚠️ Matn juda uzun. 4000 belgidan kamroq yuboring.")
            return

        # 🔍 Avtomatik tilni aniqlash va tarjima
        translated = GoogleTranslator(source='auto', target='en').translate(text)
        # Agar ingliz tilida yozilgan bo'lsa — o'zbekchaga tarjima qiladi
        if translated.lower() == text.lower():
            translated = GoogleTranslator(source='auto', target='uz').translate(text)

        bot.send_message(message.chat.id, f"🔤 Tarjima:\n\n{translated}")

    except Exception:
        bot.send_message(message.chat.id, "⚠️ Xato yuz berdi. Qayta urinib ko‘ring.")

if __name__ == "__main__":
    print("✅ Bot ishga tushdi...")
    bot.polling(none_stop=True)
