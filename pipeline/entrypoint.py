from pipeline.buffer_file import get_text
from scripts.get_job_description import get_job_description
import spacy
import os

# Load the spaCy model
nlp = spacy.load("D:\InterviewBot\models\model-last")

# Directory containing video files
video_dir = r'D:\InterviewBot\video_files'

# Path to the job description file
job_desc_path = r"D:\InterviewBot\Job Description\AI Intern- Job Description.pdf"

# Dictionary to store filename and common percentage
common_percentage_dict = {}

num_of_videos = os.listdir(video_dir)[2:5]
# Iterate over video files in the directory
for video_filename in num_of_videos:
    # Construct the full path to the video file
    video_path = os.path.join(video_dir, video_filename)

    # Process the video and job description
    text = get_text(video_path)
    job_desc = get_job_description(job_desc_path)

    # Process the job description and resume texts
    job_doc = nlp(job_desc)
    resume_doc = nlp(text)

    # Extract entities from the processed documents
    job_entities = [ent.text.lower() for ent in job_doc.ents]
    resume_entities = [ent.text.lower() for ent in resume_doc.ents]

    # Calculate common percentage
    common_words = set(job_entities) & set(resume_entities)
    num_common_words = len(common_words)
    common_percentage = (num_common_words / len(resume_entities)) * 100

    # Store the common percentage in the dictionary
    common_percentage_dict[video_filename] = common_percentage

# Print the dictionary with filenames and common percentages
sorted_common_percentage = dict(sorted(common_percentage_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionary with filenames and common percentages
for filename, score in sorted_common_percentage.items():
    print(f"Filename: {filename}, score : {score*4:.2f}")
