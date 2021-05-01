import youtube_dl
import csv

videos = []

print("Starting ytdown...")
with open('likedvideoplaylist.csv', newline='') as csvfile:
    csvlist = list(csv.reader(csvfile, delimiter=','))
    for row in csvlist[5:]:
        if len(row) >= 0:
            videos.append(row[0])

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]',
    'outtmpl': '/data/%(title)s.%(ext)s',
    'writethumbnail': True,
    'postprocessors': [
        {'key': 'EmbedThumbnail'},
        {'key': 'FFmpegMetadata'}
    ]
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(videos)
