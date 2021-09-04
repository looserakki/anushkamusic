import os
import asyncio

from pyrogram import Client, filters



@Client.on_message(filters.command("ping"))
async def ping(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hello You don't worry TG VC VIDEO STREAMER is Online\nPowered by @RobotTech_official ",   
       
                               )
                           
@Client.on_message(filters.command("ping"))
async def ping(client, m: Message):
   if m.chat.type == 'group':
       await m.reply(f"** Hello You don't worry TG VC VIDEO STREAMER is Online\nPowered by @RobotTech_official ",  
       
                                )
                            
                            
