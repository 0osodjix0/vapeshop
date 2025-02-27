from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
API_ID = 24975446  # Ваш API_ID
API_HASH = "f82c232ae1cad374182158c047133523"  # Ваш API_HASH
BOT_TOKEN = "7425011148:AAGxr_fDpQkLSOXwehufQGefT7Ig3zvr4qg"  # Ваш токен бота

bot = Client("shop_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@bot.on_message(filters.command("start"))
def start(client, message):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("Открыть магазин", web_app=WebAppInfo(url="https://2655-5-253-206-122.ngrok-free.app/index.html"))]
    ], resize_keyboard=True)

    message.reply_text("Привет! Нажми на кнопку ниже, чтобы открыть магазин:", reply_markup=keyboard)

bot.run()