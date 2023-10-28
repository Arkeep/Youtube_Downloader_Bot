from pytube import YouTube


def download_video(url: str, user_id: int):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution().download(filename=f"{user_id}")

    return video