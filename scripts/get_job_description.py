import pdfplumber

def get_job_description(pdf_path):
    # Initialize a variable to store the extracted text
    extracted_text = ''

    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Iterate through each page and extract text
        for page in pdf.pages:
            text = page.extract_text()
            # Decode the text using UTF-8 encoding
            text = text.encode("utf-8", "ignore").decode("utf-8", "ignore")
            extracted_text += text

    # Print the extracted text
    return extracted_text

if __name__ == "__main__":
    data = get_job_description("D:/InterviewBot/Job Description/AI Intern- Job Description.pdf")
    print(data)
