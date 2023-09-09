import speech_recognition as sr
import time
# Function to convert audio to text using Google Web Speech API
def google_speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Web Speech API could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Web Speech API; {e}"

# Function to convert audio to text using CMU Sphinx (offline)
def sphinx_speech_to_text(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_sphinx(audio)
        return text
    except sr.UnknownValueError:
        return "CMU Sphinx could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from CMU Sphinx; {e}"

if __name__ == "__main__":

    a = time.time()
    # Replace 'audio_path' with the path to your audio file (in WAV format for Sphinx)
    audio_path = "/Users/vansh/Desktop/VideoAssesment/audio_files/1.wav"

    # Convert audio to text using Google Web Speech API
    google_result = google_speech_to_text(audio_path)
    print("Google Web Speech API Result:")
    print(google_result)

    # Convert audio to text using CMU Sphinx (offline)
    sphinx_result = sphinx_speech_to_text(audio_path)
    print("\nCMU Sphinx Result:")
    print(sphinx_result)
    b = time.time()
    print("Execution took: ", b-a)
