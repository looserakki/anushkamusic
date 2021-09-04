import os
import asyncio
from pytgcalls import GroupCallFactory
from pyrogram import Client, filters
from pyrogram.types import Message
from config import API_ID, API_HASH, SESSION_NAME. GOLDEN_CHAMCE, BOT_USERNAME
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 



app = Client(SESSION_NAME, API_ID, API_HASH)
group_call_factory = GroupCallFactory(app, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)
VIDEO_CALL = {}

#pm message started

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**{GOLDEN_CHANCE} 𝐇𝐞𝐲 𝐢 𝐚𝐦 𝐓𝐆 𝐯𝐢𝐝𝐞𝐨 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐛𝐨𝐭. 𝐔𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐒𝐭𝐫𝐞𝐚𝐦 𝐚𝐧𝐲 𝐕𝐢𝐝𝐞𝐨 𝐢𝐧 𝐕𝐜 \n**𝐇𝐢𝐭 /help  𝐭𝐨 𝐤𝐧𝐨𝐰 𝐦𝐲 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.\n\n 𝙈𝙖𝙙𝙚 𝙗𝙮 @RobotTech_Official 𝙬𝙞𝙩𝙝 ❤",   
                            reply_markup=InlineKeyboardMarkup(
                         
                                     InlineKeyboardButton(
                                            "𝐀𝐝𝐝 𝐦𝐞 ". url="t.me/{BOT_USERNAME}
                                    ]]
                                 )
                                    
                                [[
                                     InlineKeyboardButton(
                                            "𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/RobotTech_Official")
                                    ]]
                            ))
   else:
      await m.reply("**𝙏𝙂 𝙑𝙞𝙙𝙚𝙤 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜 𝙄𝙨 𝙡𝙞𝙫𝙚 ! ✨**")

#help menu started 

@Client.on_message(filters.command("help"))
async def help(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**{GOLDEN_CHANCE} 𝐇𝐞𝐲 𝐕𝐫𝐨 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐡𝐞𝐥𝐩 𝐦𝐞𝐧𝐮 ❤\n\n𝐒𝐭𝐞𝐩1: 𝖠𝖽𝖽 𝗍𝗁𝗂𝗌 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 𝖺𝗇𝖽 𝗆𝖺𝗄𝖾 𝗁𝗂𝗆 𝖺𝖽𝗆𝗂𝗇\n𝐒𝐭𝐞𝐩2: 𝖠𝖽𝖽 𝗍𝗁𝖾 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾 𝗆𝖾𝗇𝗍𝗂𝗈𝗇𝖾𝖽 𝗂𝗇 𝖡𝗈𝗍 𝖠𝖻𝗈𝗎𝗍\n\n𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬\n/stream (reply to a video)\n/stop or /stopstream".   
                           reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/RobotTech_Official")
                                    ]]
                                    
                                  ))


# @shubham-king

@Client.on_message(filters.command("stream"))
async def stream(client, m: Message):
    replied = m.reply_to_message
    if not replied:
        await m.reply("`𝐀𝐫𝐞 𝐲𝐨𝐮 𝐤𝐢𝐝𝐝𝐢𝐧𝐠 𝐦𝐞 😑 𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐚 𝐕𝐢𝐝𝐞𝐨!`")
    elif replied.video or replied.document:
        msg = await m.reply("`𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠...`")
        chat_id = m.chat.id
        try:
            video = await client.download_media(m.reply_to_message)
            await msg.edit("`𝐌𝐞𝐫𝐠𝐢𝐧𝐠...`")
            os.system(f'ffmpeg -i "{video}" -vn -f s16le -ac 2 -ar 48000 -acodec pcm_s16le -filter:a "atempo=0.81" vid-{chat_id}.raw -y')
        except Exception as e:
            await msg.edit(f"**𝐁𝐨𝐭 𝐆𝐞𝐭 𝐅𝐮𝐜𝐤𝐞𝐝 \n 𝐕𝐢𝐬𝐢𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐜𝐡𝐚𝐭** - `{e}`")
        await asyncio.sleep(5)
        try:
            group_call = group_call_factory.get_file_group_call(f'vid-{chat_id}.raw')
            await group_call.start(chat_id)
            await group_call.set_video_capture(video)
            VIDEO_CALL[chat_id] = group_call
            await msg.edit("**▶ 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠..**")
        except Exception as e:
            await msg.edit(f"**𝐆𝐨𝐭 𝐅𝐮𝐜𝐤𝐞𝐝 𝐨𝐧𝐜𝐞 𝐦𝐨𝐫𝐞.** -- `{e}`")
    else:
        await m.reply("`𝐈 𝐚𝐦 𝐛𝐞𝐢𝐧𝐠 𝐟𝐮𝐜𝐤𝐢𝐧𝐠 𝐑𝐞𝐩𝐥𝐲 𝐭𝐨 𝐯𝐢𝐝𝐞𝐨!`")

@Client.on_message(filters.command("stop"))
async def stopvideo(client, m: Message):
    chat_id = m.chat.id
    try:
        await VIDEO_CALL[chat_id].stop()
        await m.reply("**𝐒𝐭𝐨𝐩𝐞𝐝 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠**")
    except Exception as e:
        await m.reply(f"**𝐈 𝐚𝐦 𝐠𝐞𝐭𝐭𝐢𝐧𝐠 𝐅𝐮𝐜𝐤𝐞𝐝 # 𝐄𝐫𝐫𝐨𝐫** - `{e}`")
