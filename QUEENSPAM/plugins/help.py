from QUEENSPAM import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from QUEENSPAM import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/e2f9ebb8153b2e08ef433.jpg"

QUEEN_Help = " ✨ 𝗤𝘂𝗲𝗲𝗻 𝗦𝗽𝗮𝗺 𝗕𝗼𝘁 🥀 \n\n"
 
QUEEN_Help += f"__ᴄᴍɴᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ Qᴜᴇᴇɴ ʙᴏᴛ__\n\n"

QUEEN_Help += f" ๏ ᴜꜱᴇʀʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅꜱ\n\n"

QUEEN_Help += f" ➻ `!ping` - ᴛᴏ ᴄʜᴇᴄᴋ ᴘɪɴɢ\ɴ ➻ `!alive` - ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ ᴀʟɪᴠᴇ/ᴠᴇʀꜱɪᴏɴ (ᴏɴʟʏ ᴍᴀɪɴ ᴜꜱᴇʀʙᴏᴛ ᴡɪʟʟ ʀᴇᴘʟʏ)\n ➻ `!restart` - ᴛᴏ ʀᴇꜱᴛᴀʀᴛ ᴀʟʟ ꜱᴘᴀᴍ ʙᴏᴛꜱ \n `!addecho` - ᴛᴏ ᴀᴅᴅᴇᴄʜᴏ \n `!recho` - ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴇᴄʜᴏ \n `!addsudo` - ᴛᴏ ᴀᴅᴅ ꜱᴜᴅᴏ ᴜꜱᴇʀ ᴜꜱɪɴɢ ꜱᴘᴀᴍ ʙᴏᴛ \n\n"
 
QUEEN_Help += f" ๏ ʟᴇᴀᴠᴇ ᴄᴏᴍᴍᴀɴᴅꜱ\n\n"

QUEEN_Help += f" ➻ `!leave` - ᴛᴏ ʟᴇᴀᴠᴇ ᴘᴜʙʟɪᴄ/ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘꜱ\n\n"
 
QUEEN_Help += f" ๏ ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ\n\n"

QUEEN_Help += f" ➻ `!raid` - ᴛᴏ ʀᴀɪᴅ\n ➻ `!replyraid` - ᴛᴏ ᴀᴄᴛɪᴠᴇ ʀᴇᴘʟʏ ʀᴀɪᴅ\n ➻ `!queenraid` - ᴛᴏ ᴅᴇ-ᴀᴄᴛɪᴠᴇ ʀᴇᴘʟʏ ʀᴀɪᴅ\n ➻ `!spam` - ᴛʜɪꜱ ᴄᴍᴅ ᴜꜱᴇ ꜰᴏʀ ɴᴏʀᴍᴀʟ ꜱᴘᴀᴍ\n ➻ `!bigspam` - ᴛʜɪꜱ ᴄᴍᴅ ᴜꜱᴇ ꜰᴏʀ ʙɪɢ ꜱᴘᴀᴍ\n ➻ `!uspam` - ᴛʜɪꜱ ᴄᴍᴅ ᴜꜱᴇ ꜰᴏʀ ᴜɴʟɪᴍɪᴛᴇᴅ ꜱᴘᴀᴍ ᴜɴᴛɪʟ ʏᴏᴜ ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛꜱ!!\n ➻ `!queenspam` - ᴛʜɪꜱ ᴄᴍᴅ ᴜꜱᴇ ꜰᴏʀ Qᴜᴇᴇɴ ꜱᴘᴀᴍ\n\n"

QUEEN_Help += f" !queenspam - ɪ ᴡɪʟʟ ꜱᴜɢɢᴇꜱᴛ ᴅᴏɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ \n\n"

QUEEN_Help += f"© @TheQueenBots\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=QUEEN_Help,
                                  buttons=[
        [
        Button.url("°ᴄʜᴀɴɴᴇʟ°", "https://t.me/QUEEN_NETWORK")
        ] 
        ]
        )
