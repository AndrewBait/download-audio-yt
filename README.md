# YouTube Audio Downloader

Este projeto permite baixar o áudio de vídeos do YouTube em formato MP3 usando `yt-dlp`.

## Requisitos

- **Python 3.6+**
- **yt-dlp** (instalado através do `requirements.txt`)
- **ffmpeg** (para conversão de áudio para MP3)

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Baixe e instale o [FFmpeg](https://ffmpeg.org/download.html), necessário para converter o áudio em MP3.
    - Após o download, adicione o diretório `bin` do FFmpeg ao PATH do sistema para que o `yt-dlp` possa utilizá-lo.

## Uso

Execute o script `main.py` para baixar o áudio de um vídeo do YouTube:

```bash
python main.py
```

Cole o link do vídeo quando solicitado e aguarde o download.

```bash
Cole aqui sua URL: https://www.youtube.com/watch?v=exemplo
Baixando apenas o áudio...
Download concluído: Nome_do_Video.mp3
```

## Erros Comuns

Postprocessing: ffprobe and ffmpeg not found: Certifique-se de que o FFmpeg está instalado e incluído no PATH do sistema.

