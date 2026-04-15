import yt_dlp

def get_stream(name):
    ydl_opts = {
        "format": "bestaudio",
        "quiet": True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{name}", download=False)

        if not info.get('entries'):
            return None, None
        
        video = info['entries'][0]

        return video['webpage_url'], video['title']