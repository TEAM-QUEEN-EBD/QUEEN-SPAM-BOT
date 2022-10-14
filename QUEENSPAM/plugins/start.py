
import asyncio
import os
from telethon import events, Button
from telethon.tl.custom import button
from QUEENSPAM import BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, ALIVE_PIC, OWNER_ID, OWNER_NAME

QUEEN_IMG = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/09b3f55acf9ebff6fce2c.jpg"


Queen_Button = [
        [
        Button.url("🥀Cʜᴀɴɴᴇʟ🥀", "https://t.me/QUEEN_NETWORK"),
        Button.url("💔Sᴜᴘᴘᴏʀᴛ💔", "https://t.me/QUEEN_SPAM_BOT")
        ],
        [
        Button.url("✨Rᴇᴘᴏ✨", "https://t.me/QUEEN_SPAM_BOT")
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
        creator = f"[𝗝𝝙𝗬🥀](tg://user?id={1864894033})"
        QUEEN_ON = f"""
ʜᴇʏ 🖤 ʙᴀʙʏ  {mention} 🥀,
ᴛʜɪs ɪs Qᴜᴇᴇɴ sᴘᴀᴍʙᴏᴛ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:- [Qᴜᴇᴇɴ ꜱᴘᴀᴍʙᴏᴛ!](https://t.me/QUEEN_NETWORK)
────────────────── 
➻ ᴛʜɪs ʙᴏᴛ ᴏᴡɴᴇʀ: {myOwner}
➻ Qᴜᴇᴇɴ ꜱᴘᴀᴍ ᴏᴡɴᴇʀ: [ᴍᴀꜰɪᴀ ʀᴀᴊ🥀](https://t.me/MAFIA_RJ)
➻ ᴄᴏᴅᴇ ᴄʀᴇᴀᴛᴏʀ: {creator}
────────────────── 
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴀᴄᴄᴇss sᴜᴘᴘᴏʀᴛ ,ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ʀᴇᴘᴏ!
    """
        await e.client.send_file(e.chat_id, QUEEN_IMG, caption=QUEEN_ON, buttons=Queen_Button)
