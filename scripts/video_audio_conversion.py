from moviepy.editor import VideoFileClip

video_path = 'path_to_your_video.mp4'  # Replace with your video file path
video_clip = VideoFileClip(video_path)

audio_clip = video_clip.audio

audio_output_path = 'output_audio.mp3'  # Replace with your desired output audio file path
audio_clip.write_audiofile(audio_output_path)

video_clip.close()
audio_clip.close()
