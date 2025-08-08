import json
import os
from PyPDF2 import PdfReader

pdf_path = '/Users/sadhikavarakala/Practice/Sadhika Varakala Resume.pdf'
output_path = '/Users/sadhikavarakala/Practice/Sadhika_Varakala_Resume.json'

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        reader = PdfReader(f)
        text= ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    
#convert to json

pdf_text = extract_text_from_pdf(pdf_path)

resume_json = {
    'file_name' : os.path.basename(pdf_path),
    'content' : pdf_text
}

#save 

with open(output_path, 'w') as json_file:
    json.dump(resume_json, json_file, indent=4)

print(f"PDF content extracted and saved to {output_path}")