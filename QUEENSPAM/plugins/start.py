
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from QUEENSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

QUEEN_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/09b3f55acf9ebff6fce2c.jpg"


Queen_Button = [
        [
        Button.url("ð¥CÊá´É´É´á´Êð¥", "https://t.me/QUEEN_NETWORK"),
        Button.url("ðSá´á´á´á´Êá´ð", "https://t.me/QUEEN_SPAM_BOT")
        ],
        [
        Button.url("â¨Rá´á´á´â¨", "https://t.me/QUEEN_SPAM_BOT")
        ]
        ]
        

#USERS 


@BOT0.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT1.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT2.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT3.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT4.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT5.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT6.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT7.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT8.on(events.NewMessage(incoming=True, pattern='/start'))
@BOT9.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[ððð¬ð¥](tg://user?id={1864894033})"
        QUEEN_ON = f"""
Êá´Ê ð¤ Êá´ÊÊ  {mention} ð¥,
á´ÊÉªs Éªs Qá´á´á´É´ sá´á´á´Êá´á´ á´á´á´¡á´Êá´á´ ÊÊ:- [Qá´á´á´É´ ê±á´á´á´Êá´á´!](https://t.me/QUEEN_NETWORK)
ââââââââââââââââââ 
â» á´ÊÉªs Êá´á´ á´á´¡É´á´Ê: {myOwner}
â» Qá´á´á´É´ ê±á´á´á´ á´á´¡É´á´Ê: [á´á´ê°Éªá´ Êá´á´ð¥](https://t.me/MAFIA_RJ)
â» á´á´á´á´ á´Êá´á´á´á´Ê: {creator}
ââââââââââââââââââ 
á´ÊÉªá´á´ Êá´Êá´á´¡ Êá´á´á´á´É´ á´á´ á´á´á´á´ss sá´á´á´á´Êá´ ,á´Êá´É´É´á´Ê á´É´á´ Êá´á´á´!
    """
        await e.client.send_file(e.chat_id, QUEEN_IMG, caption=QUEEN_ON, buttons=Queen_Button)
