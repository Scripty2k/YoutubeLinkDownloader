from pytube import YouTube

def download_video():
    print("Welcome to the YouTube Downloader!")
    # Ask for a YouTube link
    url = input("Enter the YouTube link: ")

    try:
        yt = YouTube(url)  # Initialize the YouTube video
        print(f"Title: {yt.title}")
        print("Choose a format:")
        print("1. MP4 (video)")
        print("2. MP3 (audio only)")
        choice = input("Make your choice (1 or 2): ")

        if choice == '1':
            # Download video (MP4)
            print("Downloading video...")
            stream = yt.streams.get_highest_resolution()
            stream.download()
            print(f"Video has been downloaded: {yt.title}.mp4")
        elif choice == '2':
            # Download audio (MP3)
            print("Downloading audio...")
            stream = yt.streams.filter(only_audio=True).first()
            output_path = stream.download()
            
            # Change the file extension to .mp3
            base, ext = output_path.rsplit('.', 1)
            new_file = base + '.mp3'
            import os
            os.rename(output_path, new_file)
            
            print(f"Audio has been downloaded: {yt.title}.mp3")
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

download_video()