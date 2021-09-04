from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 

GOLDEN_CHANCE = "https://telegra.ph/file/6969f6dac0aa325b85745.jpg"

@Client.on_message(filters.command("help"))
async def help(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**{GOLDEN_CHANCE} 𝐇𝐞𝐲 𝐕𝐫𝐨 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐡𝐞𝐥𝐩 𝐦𝐞𝐧𝐮 ❤\n\n𝐒𝐭𝐞𝐩1: 𝖠𝖽𝖽 𝗍𝗁𝗂𝗌 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 𝖺𝗇𝖽 𝗆𝖺𝗄𝖾 𝗁𝗂𝗆 𝖺𝖽𝗆𝗂𝗇\n𝐒𝐭𝐞𝐩2: 𝖠𝖽𝖽 𝗍𝗁𝖾 𝖠𝗌𝗌𝗂𝗌𝗍𝖺𝗇𝖼𝖾 𝗆𝖾𝗇𝗍𝗂𝗈𝗇𝖾𝖽 𝗂𝗇 𝖡𝗈𝗍 𝖠𝖻𝗈𝗎𝗍\n\n𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬\n/stream (reply to a video)\n/stop to stop video\n/userbotjoin To join assistance automatically\n/ping to check ping",
                           reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/RobotTech_Official")
                                    ]]
                                    
                                  ))
                                  
@Client.on_message(filters.command("help"))
async def help(client, m: Message):
   if m.chat.type == 'group':
       await m.reply(f"**{GOLDEN_CHANCE} HELLO THANKS FOR ADDING ME!\n\nIF YOU NEED HELP RELATED TO BOT COMMAND , CHECK IT IN BOT PM\n if you need support then click here",
                           reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/RobotTech_Official")
                                    ]]
                                    
                                  ))
