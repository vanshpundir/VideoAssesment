from pipeline.buffer_file import get_text
from scripts.get_job_description import get_job_description
from collections import Counter

import spacy
import os

def get_everything(video, job_desc):
    text = get_text(video)


    job_desc = get_job_description(job_desc)
    # print(job_desc)


    # Load the spaCy model
    nlp = spacy.load("D:\InterviewBot\models\model-last")


    # Process the job description and resume texts
    job_doc = nlp(job_desc)
    resume_doc = nlp(text)

    # Extract entities from the processed documents
    job_entities = [ent.text.lower()  for ent in job_doc.ents]
    print(job_entities)

    resume_entities = [ent.text.lower() for ent in resume_doc.ents]
    print(resume_entities)

    common_words = set(job_entities) & set(resume_entities)
    num_common_words = len(common_words)

    # Print the common words and the count
    print("Common Words:", common_words)
    print("Number of Common Words:", (num_common_words/len(resume_entities))*100)

    return (num_common_words/len(resume_entities))*100




