from google.cloud import speech
import io
from pydub import AudioSegment
from pydub.silence import split_on_silence

# Initialize the Google Cloud client
client = speech.SpeechClient()

# Function to convert stereo audio to mono and get its transcription
def audio_to_text(audio_path, config):
    try:
        # Load the audio file
        audio = AudioSegment.from_wav(audio_path)

        # Initialize an empty string to store the combined transcribed text
        transcribed_text = ""

        # Calculate the duration of the audio in milliseconds
        audio_duration = len(audio)

        # Split the audio into segments on silence with a maximum length of 59 seconds
        segment_length = 59000  # 59 seconds in milliseconds
        segments = [audio[i:i+segment_length] for i in range(0, audio_duration, segment_length)]

        for segment in segments:
            # Export the segment as a mono audio file
            mono_audio_path = "/Users/vansh/Desktop/VideoAssesment/scripts/audio-chunks/mono.wav"
            segment = segment.set_channels(1)
            segment.export(mono_audio_path, format="wav")

            # Read the mono audio file and process it
            with io.open(mono_audio_path, "rb") as mono_audio_file:
                content = mono_audio_file.read()

            audio = speech.RecognitionAudio(content=content)

            # Use LongRunningRecognize for longer audio files
            operation = client.long_running_recognize(config=config, audio=audio)

            # Wait for the operation to complete
            response = operation.result()

            for result in response.results:
                transcribed_text += result.alternatives[0].transcript

        return transcribed_text

    except Exception as e:
        print("An error occurred:", str(e))
        return None

if __name__ == "__main__":
    # Replace 'audio_path' with the path to your audio file (must be in WAV format)
    audio_path = "/Users/vansh/Desktop/VideoAssesment/audio_files/5.wav"

    # Define the recognition configuration outside the function
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,  # Set to the correct sample rate of your audio
        language_code="en-US",   # Replace with the desired language code
    )

    text_from_audio = audio_to_text(audio_path, config)
    if text_from_audio:
        print(text_from_audio)
        with open("/Users/vansh/Desktop/VideoAssesment/audio_text/5.txt",'w') as f:
            f.write(text_from_audio)
    else:
        print("Transcription failed.")
