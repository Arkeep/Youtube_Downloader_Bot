from aiodgram import TgBot, types, DownloadVideo, YourMessages  
from main import token, start_message
import os

DBot = TgBot(token, admin_username="Stillcrayg")
video = DownloadVideo()
logs = YourMessages()

@DBot.dispatcher.message_handler(commands=["start"])
async def start_comand(msg: types.Message):
    await DBot.send_message(msg.from_user.id, start_message)


@DBot.dispatcher.message_handler()
async def mmm(msg: types.Message):
    if msg.text.startswith("https://youtu.be/") or msg.text.startswith("https://youtube.com/"):
        logs.message(clear=False, text=f"~~~~~~~~~~~User {msg.from_user.username} download this video {msg.text}~~~~~~~~~~~", color=["Green","Green"])
        video.download_This_Video(msg.text, msg.from_user.id)
        await DBot.send_message(msg.from_user.id, "Load")
        await DBot.send_video(msg.from_user.id, msg.from_user.id)
        await DBot.send_message(msg.from_user.id, "Loaded")
    else:
        await msg.reply("Я тебя не понимаю")

    os.remove(f"{msg.from_user.id}.mp4")


if __name__ == "__main__":
    DBot.start_polling(DBot.dispatcher, on_startup=DBot.on_startup, on_shutdown=DBot.on_shutdown)
