# InterviewBot Video Analysis

This repository contains code for analyzing video content and comparing it with a job description to determine the common keywords. You can run the analysis by executing the `entrypoint.py` script.

## Prerequisites

Before running the code in this repository, make sure you have the following prerequisites installed on your system:

1. [spaCy](https://spacy.io/): You need to install spaCy and download the required language model. You can install spaCy using pip:

   ```bash
   pip install spacy
   ```

   After installing spaCy, download and install the spaCy model. You can use the following command to download the English model:

   ```bash
   python -m spacy download en_core_web_sm
   ```

2. PDF Reader: You should have a PDF reader installed on your system to extract text from job description PDF files.

## Usage

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/InterviewBot.git
   ```

2. Navigate to the repository directory:

   ```bash
   cd InterviewBot
   ```

3. Modify the paths and parameters in the `entrypoint.py` file according to your specific use case:

   ```python
   # Load the spaCy model
   pip install -r requirements.txt 
   ```

4. Run the `entrypoint.py` script:

   ```bash
   python entrypoint.py
   ```

   This script will analyze a set of video files located in the specified directory (`video_dir`) and compare the content with the job description extracted from the PDF file (`job_desc_path`). It will calculate the common keywords and their percentage match for each video file.

5. View the results:

   The script will print the results, including filenames and their corresponding common percentage scores in descending order:

   ```plaintext
   Filename: video1.mp4, score: 62.50
   Filename: video2.mp4, score: 58.33
   Filename: video3.mp4, score: 45.83
   ```

   The scores represent the percentage match between the video content and the job description. Higher scores indicate a better match.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Special thanks to [spaCy](https://spacy.io/) for providing a powerful NLP library.
- PDF text extraction is performed using external tools.