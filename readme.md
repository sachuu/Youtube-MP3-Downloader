# YouTube Audio Downloader for Mac

This tool downloads the highest quality audio from YouTube videos and saves them as MP3 files to your Desktop (or a custom folder).

## Features
- Downloads best quality audio from YouTube
- Converts to MP3 (320kbps)
- Saves to Desktop by default, or a custom path

## Requirements
- macOS
- Python 3.7+
- [ffmpeg](https://ffmpeg.org/) (for audio conversion)

## Setup Instructions

1. **Clone or Download the Repository**

   ```sh
   git clone <repo-url>
   cd youtube-music-downloader
   ```

2. **Create and Activate a Virtual Environment**

   ```sh
   python3 -m venv source
   source source/bin/activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Install ffmpeg**

   If you don't have ffmpeg, install it with Homebrew:
   ```sh
   brew install ffmpeg
   ```

## Usage

Run the downloader script:

```sh
python yt-downloader.py
```

- You will be prompted for a YouTube video URL.
- Optionally, you can provide a custom output path.
- The audio will be downloaded and saved as an MP3 file.

You can also provide the URL as a command-line argument:

```sh
python python.py "https://www.youtube.com/watch?v=example"
```

## Notes
- By default, files are saved to your Desktop unless you specify a different path.
- Make sure ffmpeg is installed and available in your PATH.

## License
MIT License
