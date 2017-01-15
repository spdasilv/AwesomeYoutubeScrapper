from __future__ import unicode_literals
from bs4 import BeautifulSoup
import youtube_dl
import urllib.request

def CreateArrayOfSongs (path):
    songs = []
    collection = open(path, 'r', encoding='utf-8-sig')
    for song in collection:
        songs.append(song)
    return songs


def GetWatchID (song):
    url = "https://www.youtube.com/results?search_query="
    query = song.rstrip('\n')
    query = urllib.request.quote(query)
    fullurl = url + query
    result = urllib.request.urlopen(fullurl)
    resultHtml = result.read()
    result.close()
    soup = BeautifulSoup(resultHtml,'html.parser')
    videos = soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ")
    watchID = videos[0].get('href')
    return watchID

songs = CreateArrayOfSongs("processed_24_dec_2015_backup.txt")
options = {
    'format': 'bestaudio/best', # choice of quality
    'extractaudio': True,      # only keep the audio
    'audioformat': "mp3",      # convert to mp3
    'outtmpl': '%(title)s',        # name the file the ID of the video
    'noplaylist': True,        # only download single song, not playlist
}
for song in songs:
    watchID = GetWatchID(song)
    with youtube_dl.YoutubeDL(options) as ydl:
        print('Downloading "'+watchID+'"')
        ydl.download(['http://www.youtube.com'+watchID])
        print('Download Complete.')
