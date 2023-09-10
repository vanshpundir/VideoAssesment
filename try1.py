from transformers import pipeline
whisper = pipeline('automatic-speech-recognition', model = 'openai/whisper-small', device = 0)
text = whisper(r'D:\InterviewBot\audio_files\3.wav')
print(text)