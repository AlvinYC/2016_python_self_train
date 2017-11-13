# pip3 freeze | grep pytube
# pytube==7.0.18
# get the following document for usage guide
# https://python-pytube.readthedocs.io/en/stable/user/quickstart.html

from pytube import YouTube
yt = YouTube('https://www.youtube.com/watch?v=RwR1uif_uDg')
print(yt.title)
print(yt.streams.all())
stream = yt.streams.first()
stream.download('./tmp')

