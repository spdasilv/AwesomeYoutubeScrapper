from cx_Freeze import setup, Executable

setup(name='GetYoutubeMP3',
      version='0.1',
      description='Use a .txt file to download multiple youtube MP3s',
      executables=[Executable("YouTubeDownloader.py")])