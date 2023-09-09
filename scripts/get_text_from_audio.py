from google.cloud import speech
import io
from pydub import AudioSegment

# Initialize the Google Cloud client
client = speech.SpeechClient()

# Function to convert stereo audio to mono and then convert it to text
def audio_to_text(audio_path):
    try:
        # Load the audio file and convert it to mono
        audio = AudioSegment.from_wav(audio_path)
        audio = audio.set_channels(1)

        # Export the mono audio as raw WAV bytes
        with io.BytesIO() as wav_buffer:
            audio.export(wav_buffer, format="wav")
            content = wav_buffer.getvalue()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,  # Set to the correct sample rate of your audio
            language_code="en-US",   # Replace with the desired language code
        )

        response = client.recognize(config=config, audio=audio)

        for result in response.results:
            print("Transcript: {}".format(result.alternatives[0].transcript))

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":


    # Replace 'audio_path' with the path to your audio file (must be in WAV format)
    audio_path = "/Users/vansh/Desktop/VideoAssesment/audio_files/1.wav"

    audio_to_text(audio_path)
