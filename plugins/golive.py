import asyncio

import pytgcalls
import pyrogram
from pyrogram import Client, filters
from config import API_ID, API_HASH, STREAM_URL, CHAT_ID


API_ID = 'API_ID'
API_HASH = 'API_HASH'

INPUT_SOURCE = '{STREAM_URL}'

CHAT_ID = 'CHAT_ID'




@Client.on_message(filters.command("golive"))
async def main(client):
    group_call = pytgcalls.GroupCallFactory(client).get_group_call()
    await group_call.join(CHAT_ID)
    await group_call.start_video(INPUT_SOURCE)

    await pyrogram.idle()


if __name__ == 'golive':
    pyro_client = pyrogram.Client('pytgcalls', API_ID, API_HASH)
    pyro_client.start()

    asyncio.get_event_loop().run_until_complete(main(pyro_client))
