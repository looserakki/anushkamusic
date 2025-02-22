import asyncio
from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from plugins.videoplayer import app
from plugins.videoplayer import call_py
bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
)


bot.start()
app.start()
call_py.start()
idle()
