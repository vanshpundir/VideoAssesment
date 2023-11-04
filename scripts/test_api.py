import requests

# Define the API endpoint URL
api_url = "http://localhost:5001/compare/compare-entities"

# Create a dictionary with the file data to be uploaded
files = {
    'video': ('video.mp4', open(r"C:\Users\jogin\Downloads\VIDEO-2023-09-10-13-54-01.mp4", 'rb')),
    'job_description': ('job_description.pdf', open('D:\InterviewBot\Job Description\_Voice AI - Associate  AI Engineer _Job description.pdf', 'rb'))
}

# Send a POST request to the API
response = requests.post(api_url, files=files)

# Check the response
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.status_code)
    print(response.json())
