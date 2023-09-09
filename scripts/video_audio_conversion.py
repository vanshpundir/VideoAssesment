from moviepy.editor import VideoFileClip

video_path = '/Users/vansh/Desktop/VideoAssesment/video_files/VIDEO RESUME  Pervin L Yabut.mp4'  # Replace with your video file path
video_clip = VideoFileClip(video_path)


audio_clip = video_clip.audio
print(audio_clip)

audio_output_path = '/Users/vansh/Desktop/VideoAssesment/audio_files/1.wav'  # Replace with your desired output audio file path
audio_clip.write_audiofile(audio_output_path)

video_clip.close()
audio_clip.close()
