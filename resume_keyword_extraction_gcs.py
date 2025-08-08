import json
from collections import Counter
from google.cloud import storage

BUCKET_NAME = "sadhika-1-central1"
INPUT_FILE_PATH = "data/Sadhika_Varakala_Resume.json"
OUTPUT_FILE_PATH = "data/output/resume_keywords.json"

known_skills = {
    'python', 'java', 'sql', 'excel', 'agile', 'scrum', 'machine learning', 
    'power bi', 'google cloud', 'aws', 'dataproc', 'bigquery', 'gcs', 'google cloud storage',
    'pyspark', 'spark', 'spark sql', 'git'
}

#init gcs client

client = storage.Client()
bucket = client.bucket(BUCKET_NAME)

# read json file from GCS
blob = bucket.blob(INPUT_FILE_PATH)
resume_text = blob.download_as_text().lower()

#count skills
skill_counter = Counter()

for skill in known_skills:
    if skill in resume_text:
        count = resume_text.count(skill)
        skill_counter[skill] = count

#write output to gcs
output_blob = bucket.blob(OUTPUT_FILE_PATH)
output_blob.upload_from_string(
    data=json.dumps(skill_counter, indent=4),
    content_type='application/json'
)

print(f"Resume keywords extracted and saved to {OUTPUT_FILE_PATH} in bucket {BUCKET_NAME}")