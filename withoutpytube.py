import requests

def download_video(video_url, output_file):
    try:
        # Send a GET request to the video URL
        response = requests.get(video_url, stream=True)
        response.raise_for_status()  # Check for request errors

        # Open a file to write the video content
        with open(output_file, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Video successfully downloaded to {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Ask the user for the video URL
video_url = input("Enter the direct video URL: ")
output_file = "downloaded_video.mp4"

download_video(video_url, output_file)
