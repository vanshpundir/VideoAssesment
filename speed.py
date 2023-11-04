# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
audio_file= open(r"D:\InterviewBot\audio_files\2.wav", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)