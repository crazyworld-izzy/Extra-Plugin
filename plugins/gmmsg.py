import re
from pyrogram import filters
import random
from VIPMUSIC import app

def get_random_video():
    videos = [
        "https://telegra.ph/file/2c63e594336bfab096835.mp4", # video 1
        "https://telegra.ph/file/8e5a08a654079fef23659.mp4", # video 2
        "https://telegra.ph/file/7dd498fb3c0ddd6c17e84.mp4", # video 3
        "https://telegra.ph/file/941f1237d433974398b12.mp4",
    ]
    return random.choice(videos)


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
    send_video = random.choice([True, False])
    if send_video:
        video_id = get_random_video()
        await app.send_video(message.chat.id, video_id)
        await message.reply_text(f"**𝒢𝑜𝑜𝒹 𝑀𝑜𝓇𝓃𝒾𝓃𝑔, {sender} 𝐻𝒶𝓋𝑒 𝒜 𝐵𝓁𝑒𝓈𝓈𝑒𝒹 𝒟𝒶𝓎 🥰**")
    else:
        emoji = get_random_emoji()
        try:
           await message.react(emoji)
        except:
        	pass
        await message.reply_text(f"**𝒢𝑜𝑜𝒹 𝑀𝑜𝓇𝓃𝒾𝓃𝑔, {sender}𝐻𝒶𝓋𝑒 𝒜 𝐵𝓁𝑒𝓈𝓈𝑒𝒹 𝒟𝒶𝓎 {emoji}**")