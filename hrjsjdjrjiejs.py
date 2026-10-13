import os
import telebot
from telebot import types
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в .env файле!")

bot = telebot.TeleBot(BOT_TOKEN)

# Ссылки
LINKS = [
    "https://t.me/+Uzd2O-2AR_M4ZWYx",
    "https://t.me/+Uzd2O-2AR_M4ZWYx",
    "https://t.me/+Uzd2O-2AR_M4ZWYx"
]

# Reply-клавиатура с кнопкой кубика
def main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dice_btn = types.KeyboardButton("🎲 Бросить кубик")
    keyboard.add(dice_btn)
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "Вот ваша ссылка на канал:\n\n"
    text += "\n".join(LINKS)
    bot.send_message(message.chat.id, text, reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: message.text == "🎲 Бросить кубик")
def send_dice(message):
    bot.send_dice(message.chat.id, reply_markup=main_keyboard())

if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)