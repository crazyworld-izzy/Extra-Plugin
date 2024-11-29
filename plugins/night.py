import re
from pyrogram import filters
import random
from VIPMUSIC import app

def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAIUG2dKAAHoSq62dFqSmzkAATF2M6MHKZUAAi8QAALidVBV7KjurHhZEHceBA", # Sticker 1
        "CAACAgUAAxkBAAIUHGdKARnWNB1K7Us9DtUYsm9VCmDBAAIHCQACq6yJV0lq6JFdFk7rHgQ", # Sticker 2
        "CAACAgUAAxkBAAIUHWdKAVFB3ASADZLU6WBdKpGxEfDsAAItBwACMioRVU2QKqJY2MwIHgQ", # Sticker 3
        "CAACAgUAAxkBAAIUHmdKAV221ESbA629y258T9poZsBCAALnCQACN0cYVQX7GHjhnQyQHgQ", # Sticker 4
        "CAACAgUAAxkBAAIUH2dKAdAzcCuO1CTuhIb9BPZebV7LAAIwBwAC-gUYVaSthhCMWXJfHgQ", # Sticker 5
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "🥰",
        "🥱",
        "🤗",
    ]
    return random.choice(emojis)

###### GOOOD MORNING 
@app.on_message(filters.command(["ood night","ood night","i8","weet dreams","weet dreams","i8","n","n"], prefixes=["g","G","n","N","s","S","g","G"]))
async def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        await app.send_sticker(message.chat.id, sticker_id)
        await message.reply_text(f"**𝐂ʜʟᴍ 𝐕.ᴄᴀʟʟ 𝐏ᴇᴀsᴀʟᴀᴍ 𝐏ᴀʀᴛʜᴀ 𝐀ᴛʜᴜᴋᴜʟʟᴀ 𝐓ʜᴜɴɢᴀ 𝐏ᴏʀɪʏᴇᴀ 🥺😢👩‍🦯 {sender} 𝐂ʜᴇʀʀɪ 𝐁ʙʏ 𝐍ᴀᴍᴍᴀ 𝐃ʀᴇᴀᴍ 𝐋ᴀ 𝐑ᴏᴍᴀɴᴄᴇ 𝐏ᴀɴɴᴀʟʟᴀᴍ 🙈😏❤️**")
    else:
        emoji = get_random_emoji()
        try:
           await message.react(emoji)
        except:
        	pass
        await message.reply_text(f"**𝐂ʜʟᴍ 𝐕.ᴄᴀʟʟ 𝐏ᴇᴀsᴀʟᴀᴍ 𝐏ᴀʀᴛʜᴀ 𝐀ᴛʜᴜᴋᴜʟʟᴀ 𝐓ʜᴜɴɢᴀ 𝐏ᴏʀɪʏᴇᴀ 🥺😢👩‍🦯 {sender}𝐂ʜᴇʀʀɪ 𝐁ʙʏ 𝐍ᴀᴍᴍᴀ 𝐃ʀᴇᴀᴍ 𝐋ᴀ 𝐑ᴏᴍᴀɴᴄᴇ 𝐏ᴀɴɴᴀʟʟᴀᴍ 🙈😏❤️ {emoji}**")
