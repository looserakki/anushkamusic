from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 


@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**{GOLDEN_CHANCE} 𝐇𝐞𝐲 𝐢 𝐚𝐦 𝐓𝐆 𝐯𝐢𝐝𝐞𝐨 𝐒𝐭𝐫𝐞𝐚𝐦𝐢𝐧𝐠 𝐛𝐨𝐭. 𝐔𝐬𝐞 𝐦𝐞 𝐭𝐨 𝐒𝐭𝐫𝐞𝐚𝐦 𝐚𝐧𝐲 𝐕𝐢𝐝𝐞𝐨 𝐢𝐧 𝐕𝐜 \n**𝐇𝐢𝐭 /help  𝐭𝐨 𝐤𝐧𝐨𝐰 𝐦𝐲 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬.\n\n 𝙈𝙖𝙙𝙚 𝙗𝙮 @RobotTech_Official 𝙬𝙞𝙩𝙝 ❤",   
                            reply_markup=InlineKeyboardMarkup(
                         
                                     InlineKeyboardButton(
                                            "𝐀𝐝𝐝 𝐦𝐞 ". url="t.me/{BOT_USERNAME}")
                                    ]]
                                 )
                                    
                                [[
                                     InlineKeyboardButton(
                                            "𝐒𝐮𝐩𝐩𝐨𝐫𝐭", url="t.me/RobotTech_Official")
                                    ]]
                            ))
                            
