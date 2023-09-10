# from pipeline.get_text_from_audio import audio_to_text
# from google.cloud import speech
# from pipeline.video_audio_conversion import get_audio
#
# import os
#
# for i in os.listdir("/Users/vansh/Desktop/VideoAssesment/video_files"):
#     get_audio(os.path.join("/Users/vansh/Desktop/VideoAssesment/video_files", i), i)
#     audio_path = f"/Users/vansh/Desktop/VideoAssesment/audio_files/{i}.wav"
#
#     # Define the recognition configuration outside the function
#     config = speech.RecognitionConfig(
#         encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#         sample_rate_hertz=44100,  # Set to the correct sample rate of your audio
#         language_code="en-US",  # Replace with the desired language code
#     )
#     text_from_audio = audio_to_text(audio_path, config)
#     if text_from_audio:
#         with open (f"/Users/vansh/Desktop/VideoAssesment/audio_text/{i}.txt", 'w') as f:
#             f.write(text_from_audio)
#         print(text_from_audio)
#     else:
#         print("Transcription failed.")


