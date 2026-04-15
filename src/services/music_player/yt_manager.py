import yt_dlp

def get_stream(name):
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'quiet': True,
        'noplaylist': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{name}", download=False)

        if not info.get('entries'):
            return None, None
        
        print(f"INFOR: {info}")
        video = info['entries'][0]
        print(f"VIDEOR: {video}")
        return video['url'], video['title']