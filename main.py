from typing import *
import random
from mojang import MojangAPI

from fastapi import *
from fastapi.responses import *
from youtube_dl import YoutubeDL
YDL_OPTIONS = {'netrc':'$HOME/.netrc', 'format':'bestaudio/best', 'audio_format':'flac', 'audio_quality':'0', 'extract_audio':'True', 'noplaylist':'True', 'no_warnings':'True'}

def ydl_url(url):
    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)

    URL = info['formats'][0]['url']
    return URL

app = FastAPI()


@app.get("/")
async def main():
    return FileResponse("index.html")

@app.get("/youtube-dl")
async def youtube_dl(url: str):
    URL = ydl_url(url)
    return HTMLResponse(content=f"""{URL}""", status_code=200)
