import speech_recognition as sr
from pydub import AudioSegment
from pydub.silence import split_on_silence


import os
r = sr.Recognizer()



def transcribe_large_audio(path):
    """Split audio into chunks and apply speech recognition"""
    # Open audio file with pydub
    sound = AudioSegment.from_wav(path)

    # Split audio where silence is 700ms or greater and get chunks
    chunks = split_on_silence(sound, min_silence_len=1500, silence_thresh=sound.dBFS-14, keep_silence=700)
    
    # Create folder to store audio chunks
    folder_name = "audio-chunks"
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


    whole_text = ""
    # Process each chunk


    # Return text for all chunks
    return whole_text

if __name__ == "__main__":
    result = transcribe_large_audio('/Users/vansh/Desktop/VideoAssesment/audio_files/1.wav')

    print(result)
