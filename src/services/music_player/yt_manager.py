import yt_dlp

def get_stream(name):
    with yt_dlp.YoutubeDL({'format': 'bestaudio', 'quiet': True}) as ydl:
        info = ydl.extract_info(f"ytsearch:{name}", download=False)

        if not info.get('entries'):
            return None, None

        video = info['entries'][0]
        print(video)
        return video['url'], video['title']