from os import path

from yt_dlp import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"<b>🚫 𝚅𝙸𝙳𝙴𝙾 𝙸𝚂 𝙻𝙾𝙽𝙶𝙴𝚁 𝚃𝙷𝙰𝙽 {DURATION_LIMIT} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂(𝚂). 𝚂𝙴𝙽𝙳 𝚂𝙷𝙾𝚁𝚃𝙴𝚁 𝚅𝙾𝙳𝙴𝙾, 𝙲𝙰𝙽'𝚃 𝙿𝙻𝙰𝚈.𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝙳 𝚅𝙸𝙳𝙴𝙾 𝙸𝚂 {duration} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂(𝚂)</b>"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
