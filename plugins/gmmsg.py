import re
from pyrogram import filters
import random
from VIPMUSIC import app

def get_random_sticker():
    stickers = [
        "CAACAgUAAx0CeympyQAC27tnSLpbHB1FoZu8VLPeIbi2GqK5mQACCAoAAtnGEVUI8XD0aKvG9B4E", # Sticker 1
        "CAACAgUAAx0CeympyQAC27tnSLpbHB1FoZu8VLPeIbi2GqK5mQACCAoAAtnGEVUI8XD0aKvG9B4E", # Sticker 2
        "CAACAgUAAx0CeympyQAC27tnSLpbHB1FoZu8VLPeIbi2GqK5mQACCAoAAtnGEVUI8XD0aKvG9B4E", # Sticker 3
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
@app.on_message(filters.command(["m","oodmorning"], prefixes=["g","G"]))
async def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        await app.send_sticker(message.chat.id, video_id)
        await message.reply_text(f"**𝒢𝑜𝑜𝒹 𝑀𝑜𝓇𝓃𝒾𝓃𝑔, {sender} 𝐻𝒶𝓋𝑒 𝒜 𝐵𝓁𝑒𝓈𝓈𝑒𝒹 𝒟𝒶𝓎 🥰**")
    else:
        emoji = get_random_emoji()
        try:
           await message.react(emoji)
        except:
        	pass
        await message.reply_text(f"**𝒢𝑜𝑜𝒹 𝑀𝑜𝓇𝓃𝒾𝓃𝑔, {sender}𝐻𝒶𝓋𝑒 𝒜 𝐵𝓁𝑒𝓈𝓈𝑒𝒹 𝒟𝒶𝓎 {emoji}**")
