from moviepy.editor import VideoFileClip

def get_audio(video_path, audio_output_path):
    video_clip = VideoFileClip(video_path)


    audio_clip = video_clip.audio
 # Replace with your desired output audio file path
    audio_clip.write_audiofile(audio_output_path)

    video_clip.close()
    audio_clip.close()

if __name__ == "__main__":
    video_path = '/Users/vansh/Desktop/VideoAssesment/video_files/64df6d6037474b7838448796.mp4'
    audio_output_path = '/Users/vansh/Desktop/VideoAssesment/audio_files/5.wav'
    get_audio(video_path, audio_output_path)
