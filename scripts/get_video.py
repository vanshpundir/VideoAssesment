from pytube import YouTube

# Function to download a video
def download_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Choose the highest resolution stream (you can change this as needed)
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=save_path)

        print("Video downloaded successfully!")
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    # Replace 'video_url' with the URL of the video you want to download
    video_url = "https://www.youtube.com/watch?v=your_video_id_here"

    # Replace 'save_path' with the path where you want to save the downloaded video
    save_path = "path_to_save_video"

    download_video(video_url, save_path)
