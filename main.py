import yt_dlp

def download_audio(url):
    # Opções para baixar somente o áudio
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Salva com o título do vídeo
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Download concluído: {info['title']}.mp3")
    except Exception as e:
        print(f"Erro: {e}")

# Recebe a URL do usuário e inicia o download
url = input("Cole aqui sua URL: ")
download_audio(url)
