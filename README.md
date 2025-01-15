# YouTube Downloader

This script allows you to download videos or audio from YouTube using the `pytube` library.

## How to Use

1. Run the `requirements_installer.py` script to install the necessary packages:
   ```
   python requirements_installer.py
   ```
2. Run the `youtube.py` script.
3. Enter the YouTube link when prompted.
4. Choose the format you want to download:
   - Enter `1` to download the video in MP4 format.
   - Enter `2` to download the audio in MP3 format.

## Script Details

- The script initializes a YouTube object using the provided URL.
- It displays the title of the video.
- Based on the user's choice, it either downloads the highest resolution video or the audio only.
- If the audio is downloaded, the script converts the file to MP3 format.

## Error Handling

- The script includes basic error handling to catch and display any exceptions that occur during the download process.

## Example

```
Welcome to the YouTube Downloader!
Enter the YouTube link: <Enter YouTube URL>
Title: <Video Title>
Choose a format:
1. MP4 (video)
2. MP3 (audio only)
Make your choice (1 or 2): <Enter 1 or 2>
```

## Requirements

- `pytube` library: Install it using `pip install pytube`.

# Video Downloader without pytube

This script allows you to download videos directly using the `requests` module.

## How to Use

1. Run the `requirements_installer.py` script to install the necessary packages:
   ```
   python requirements_installer.py
   ```
2. Run the `withoutpytube.py` script.
3. Enter the direct video URL when prompted.

## Script Details

- The script sends a GET request to the provided video URL.
- It writes the video content to a file named `downloaded_video.mp4`.

## Error Handling

- The script includes basic error handling to catch and display any exceptions that occur during the download process.

## Example

```
Enter the direct video URL: <Enter Video URL>
Video successfully downloaded to downloaded_video.mp4
```

## Requirements

- `requests` library: Install it using `pip install requests`.
