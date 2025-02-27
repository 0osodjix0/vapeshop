from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from fastapi import FastAPI

app = FastAPI()
API_ID = 24975446
API_HASH = "f82c232ae1cad374182158c047133523"
BOT_TOKEN = "7425011148:AAGxr_fDpQkLSOXwehufQGefT7Ig3zvr4qg"

bot = Client("shop_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("Открыть магазин", web_app=WebAppInfo(url="http://127.0.0.1:8000/index.html"))]
    ], resize_keyboard=True)

    message.reply_text("Привет! Нажми на кнопку ниже, чтобы открыть магазин:", reply_markup=keyboard)

bot.run()