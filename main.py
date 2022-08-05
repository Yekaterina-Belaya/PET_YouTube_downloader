from pytube import YouTube

link = input("Paste the link to the video: ")
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download("C:/Users/belos/Desktop/бэк/for PET_YouTube_downloader")
