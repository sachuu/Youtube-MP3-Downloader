"""
YouTube Audio Downloader for Mac
Downloads the highest quality audio from YouTube videos and saves as MP3 to Desktop
"""

import os
import sys
from pathlib import Path
import yt_dlp
import re

def sanitize_filename(filename):
    """Remove or replace characters that aren't safe for filenames"""
    # Remove or replace problematic characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    filename = re.sub(r'[\n\r\t]', ' ', filename)
    # Limit length to avoid filesystem issues
    if len(filename) > 200:
        filename = filename[:200]
    return filename.strip()

def download_youtube_audio(url, output_path=None):
    """
    Download audio from YouTube video in highest quality and convert to MP3
    
    Args:
        url (str): YouTube video URL
        output_path (str): Optional custom output path, defaults to Desktop
    """
    
    # Set default output path to Desktop if not provided
    if output_path is None:
        desktop_path = Path.home() / "Desktop"
        output_path = str(desktop_path)
    
    # Ensure output directory exists
    os.makedirs(output_path, exist_ok=True)
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best quality audio
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',  # Highest MP3 quality
        }],
        'postprocessor_args': [
            '-ar', '44100',  # Sample rate
        ],
        'prefer_ffmpeg': True,
        'keepvideo': False,  # Don't keep the video file
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Get video info first
            print("Fetching video information...")
            info = ydl.extract_info(url, download=False)
            title = sanitize_filename(info.get('title', 'Unknown'))
            duration = info.get('duration', 0)
            
            print(f"Title: {title}")
            print(f"Duration: {duration // 60}:{duration % 60:02d}")
            print(f"Output location: {output_path}")
            print("\nStarting download...")
            
            # Download and convert
            ydl.download([url])
            
            print(f"\n✅ Successfully downloaded: {title}.mp3")
            print(f"📁 Saved to: {output_path}")
            
    except yt_dlp.DownloadError as e:
        print(f"❌ Download error: {str(e)}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        return False
    
    return True

def main():
    """Main function to handle command line usage"""
    print("🎵 YouTube Audio Downloader for Mac")
    print("=" * 40)
    
    # Check if URL was provided as command line argument
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
    else:
        # Prompt user for URL
        video_url = input("Enter YouTube video URL: ").strip()
    
    if not video_url:
        print("❌ No URL provided!")
        return
    
    # Validate URL (basic check)
    if not ('youtube.com' in video_url or 'youtu.be' in video_url):
        print("❌ Please provide a valid YouTube URL")
        return
    
    # Optional: Ask for custom output path
    custom_path = input("Enter custom output path (or press Enter for Desktop): ").strip()
    output_path = custom_path if custom_path else None
    
    # Download the audio
    success = download_youtube_audio(video_url, output_path)
    
    if success:
        print("\n🎉 Download completed successfully!")
    else:
        print("\n💥 Download failed!")

if __name__ == "__main__":
    main()