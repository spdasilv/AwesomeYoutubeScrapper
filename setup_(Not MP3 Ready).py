from cx_Freeze import setup, Executable

setup(name='GetYoutubeSoundFile',
      version='0.1',
      description='Use a .txt file to download multiple youtube sound files',
      executables=[Executable("YouTubeDownloader_(Not MP3 Ready).py")])