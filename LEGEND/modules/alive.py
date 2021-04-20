# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOY
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/a4d521221d7fc1c114f1f.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "HELLO THIS IS SAVAGE OFFICIAL \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "SAVAGE OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER : [SAMEER](https://t.me/SAMEER_795) ☺️\n\n"
  LEGENDX += "FULLY UPDATED\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/SAMEER_795"), Button.url("DEVLOPER", "https://t.me/SAMEER_795")]]

  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by @sameer_795 🔥
  PROBOYX = [[Button.url("REPO-SAVAGE-USERBOT", "https://github.com/SAMEERPANTHI/savage-is-back"), Button.url("OWNER", "@SAMEER_795")]]
  
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=@SAMEER_795)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX22 and PROBOY22 🔥
  LEGENDX = "HELLO THIS IS SAVAGE OFFICIAL \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "SAVAGE OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER : [SAMEER](https://t.me/SAMEER_795) ☺️\n\n"
  LEGENDX += "FULLY UPDATED BOT\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/SAMEER_795"), Button.url("DEVLOPER", "https://t.me/SAMEER_795")]]
 await event.edit(text=SAMEER, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF SAVAGE USERBOT", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/SAMEERPANTHI/SAVAGE-IS-BACK")]])


__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
