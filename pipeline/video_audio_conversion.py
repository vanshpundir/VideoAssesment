import os
from moviepy.editor import VideoFileClip

def get_audio(video_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio

    # Extract the directory and filename from the video path
    video_dir, video_filename = os.path.split(video_path)

    # Create the audio output directory if it doesn't exist
    audio_output_dir = os.path.join(video_dir, 'audio_files')
    os.makedirs(audio_output_dir, exist_ok=True)

    # Construct the audio output path
    audio_output_path = os.path.join(audio_output_dir, video_filename.replace('.mp4', '.wav'))

    # Write the audio file
    audio_clip.write_audiofile(audio_output_path)

    video_clip.close()
    audio_clip.close()
    return audio_output_path

if __name__ == "__main__":
    video_path = '/Users/vansh/Desktop/VideoAssesment/video_files/64df6d6037474b7838448796.mp4'
    get_audio(video_path)
