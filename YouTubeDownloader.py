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
    soup = BeautifulSoup(resultHtml,'lxml')
    videos = soup.find_all("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ")
    watchID = videos[0].get('href')
    return watchID

songs = CreateArrayOfSongs("processed_24_dec_2015_backup.txt")
options = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
for song in songs:
    try:
        watchID = GetWatchID(song)
        with youtube_dl.YoutubeDL(options) as ydl:
            print('Downloading "'+watchID+'"')
            ydl.download(['http://www.youtube.com'+watchID])
            print('Download Complete.')
    except Exception as e:
        print("Error {0}".format(str(e)))
        print('Unable to obtain the song "'+song+'"')
        continue
