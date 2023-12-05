from pytube import YouTube


def download_video(url):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download()
        print("Видео успешно скачано")
    except Exception as e:
        print("Произошла ошибка при скачивании видео:", e)


if __name__ == "__main__":
    video_url = input("Введите URL видео на YouTube: ")
    download_video(video_url)

