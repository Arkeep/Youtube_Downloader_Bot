from aiogram import *
from config import *
from pytube import YouTube
import os, sys
from msgs import start_msg, start_download
import colorama
from script import download_video

@dp.message_handler(commands=["start"])
async def start_message(message: types.Message):
    await message.answer(start_msg())

@dp.message_handler()
async def text_message(message: types.Message):
    user_id = message.from_user.id
    url = message.text
    yt = YouTube(url)

    try:
        if message.text.startswith("https://youtu.be/") or message.text.startswith("https://www.youtube.com/"):
            print(colorama.Fore.LIGHTGREEN_EX + f"\nПользователь @{message.from_user.username} хочет скачать видео ~* {yt.title} *~ !")
            await message.answer(start_download(yt.title, yt.author, yt.channel_url))
            await download_youtube_video(url, user_id, message)
            
        else:
            await message.reply("Я тебя не понимаю")
        
    except Exception as e:
        print(colorama.Fore.RED + f"\n{e}\n" + colorama.Fore.RESET)


async def download_youtube_video(url: str, user_id: int, msg: types.Message):
    video = download_video(url, user_id)

    with open(f"{user_id}", "rb") as video:
        await msg.answer_video(video, caption="Твоё видео")
        os.remove(f"{user_id}")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
async def on_startup(dp: Dispatcher):
    print(colorama.Fore.GREEN + f"~~~~~~ BOT WAS STARTED @{(await dp.bot.get_me()).username} ~~~~~~")
    print(colorama.Fore.LIGHTGREEN_EX + "~~~~~~ Bot developer @Stillcrayg ~~~~~~" + colorama.Fore.RESET)



async def on_shutdown(dp: Dispatcher):

    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")
    
    print(colorama.Fore.RED + f"~~~~~~ Bot was stopped! ~~~~~~\n" + colorama.Fore.RESET)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)