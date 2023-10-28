def start_msg():
    text = """
Привет, я могу скачивать видео с YouTube
Отправь мне ссылку на видео, которое хочешь скачать!"""

    return text


def start_download(title, author, channel_url) -> str:
    text = f"""
Запуск скачивания: {title}
С канала : {author}
{channel_url}"""
    
    return text