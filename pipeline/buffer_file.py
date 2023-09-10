from pipeline.video_audio_conversion import get_audio
from pydub import AudioSegment
from pipeline.get_text_from_audio import getTextFromAudio
import os

# Input video file


def get_text(video_link):
# Get the audio from the video
    audio_path = get_audio(video_link)
    audio = AudioSegment.from_wav(audio_path)

    # Define the maximum segment duration in milliseconds (50 seconds)
    max_segment_duration = 40 * 1000

    # Split the audio into segments
    segments = []
    start_time = 0

    while start_time < len(audio):
        end_time = start_time + max_segment_duration
        if end_time > len(audio):
            end_time = len(audio)
        segment = audio[start_time:end_time]
        segments.append(segment)
        start_time = end_time

    # Process each segment and extract text
    string = ""
    for i, segment in enumerate(segments):
        # Save the segment to a temporary WAV file
        segment_path = f"segment_{i}.wav"
        segment.export(segment_path, format="wav")

        # Get text from the segment using your getTextFromAudio function
        segment_texts = getTextFromAudio(segment_path)

        for segment_text in segment_texts:
        # Append the text to the result string
            string += segment_text

            # Remove the temporary segment file
        os.remove(segment_path)

    # Now, the 'string' variable contains the extracted text from all segments
    return (string)

if __name__ == "__main__":
    video_link = r"D:\InterviewBot\video_files\64e468630910b8b3ba1ef3dd.mp4"
    print(get_text(video_link))