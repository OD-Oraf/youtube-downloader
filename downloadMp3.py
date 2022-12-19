from pytube import YouTube
import os


def download_mp3(url):
    yt = YouTube(str(url))
    video = yt.streams.filter(only_audio=True).last()

    destination = "/home/od/Documents/Python/youtubeDownload/songs"

    out_file = video.download(output_path=destination)

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(yt.title + " has been successfully downloaded")


urls = open("urls.txt", "r")
for url in urls:
    download_mp3(url)

urls.close()