from pipeline.buffer_file import get_text
from scripts.get_job_description import get_job_description
import spacy
import os

from confidence_evaluation import get_emotion
import openai
openai.api_base = 'http://localhost:1234/v1'
openai.api_key = ''
prefix = "### Instruction:\n"
suffix = "\n### Response:"

# Load the spaCy model
nlp = spacy.load("D:\InterviewBot\models\model-last")

# Directory containing video files
video_dir = r'D:\InterviewBot\video_files'

# Path to the job description file
job_desc_path = r"D:\InterviewBot\Job Description\AI Intern- Job Description.pdf"

# Dictionary to store filename and common percentage
common_percentage_dict = {}

num_of_videos = os.listdir(video_dir)[0:1]
# Iterate over video files in the directory

def get_completion(prompt, model = "local model",temperature =0.0):
    formatted_prompt =f"{prefix}{prompt}{suffix}"
    messages = [{"role": "user", "content": formatted_prompt}]
    print("you prompted", prompt)
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = temperature
    )
    return response.choices[0].message['content']


for video_filename in num_of_videos:
    # Construct the full path to the video file
    video_path = r"C:\Users\jogin\Downloads\2110993881.mp4"
    # Process the video and job description
    text = get_text(video_path)
    job_desc_key = get_completion(f"Extract comma seperated important keywords related to this resume {text}")
    print(job_desc_key.split("."))
    # print(get_completion(f"Extract comma seperated important keywords related to this resume {text}"))

    job_desc = get_job_description(job_desc_path)
    print(job_desc_key)
    print("job desc key: ", job_desc_key)
    print(get_completion(f"Extract comma seperated important keywords related to this job description {job_desc}"))

    # Process the job description and resume texts
    job_doc = nlp(job_desc)
    resume_doc = nlp(text)


    # Extract entities from the processed documents
    job_entities = [ent.text.lower() for ent in job_doc.ents]
    resume_entities = [ent.text.lower() for ent in resume_doc.ents]


    def expand_short_forms(text):
        doc = nlp(text)
        expanded_text = []
        for token in doc:
            if token.text.lower() == "ml":
                expanded_text.append("machine learning")
            elif token.text.lower() == "ai":
                expanded_text.append("artificial intelligence")
            elif token.text.lower() == "nlp":
                expanded_text.append("natural language processing")
            elif token.text.lower() == "llms":
                expanded_text.append("large language models")
            else:
                expanded_text.append(token.text)
        return " ".join(expanded_text)


    # Expand short forms in the lists
    expanded_resumes = [expand_short_forms(resume) for resume in resume_entities]
    expanded_job_descriptions = [expand_short_forms(job_desc) for job_desc in job_entities]
    print(expanded_resumes)
    # Calculate common percentage
    common_words = set(job_entities) & set(resume_entities)
    print(common_words)
    num_common_words = len(common_words)
    common_percentage = (num_common_words / len(resume_entities)) * 100

    # Store the common percentage in the dictionary
    common_percentage_dict[video_filename] = common_percentage
    # get_emotion(video_path)

# Print the dictionary with filenames and common percentages
sorted_common_percentage = dict(sorted(common_percentage_dict.items(), key=lambda item: item[1], reverse=True))

# Print the sorted dictionary with filenames and common percentages
for filename, score in sorted_common_percentage.items():
    print(f"Filename: {filename}, score : {score*4:.2f}")

