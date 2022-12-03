from pytube import YouTube

link = "https://youtu.be/Lrq6r_uSQac"
yt = YouTube(link)
print(yt.title)
print(yt.thumbnail_url)
yt = yt.streams.get_highest_resolution()
yt.download()
