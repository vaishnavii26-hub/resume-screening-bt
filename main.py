# main.py
import nltk
from utils import read_file, get_resume_scores

# Download tokenizer (run once)
nltk.download('punkt')

# Load job description
job_desc = read_file("job_description.txt")

# Score resumes
results = get_resume_scores(job_desc, "resumes")

# Sort by match score
results.sort(key=lambda x: x[1], reverse=True)

# Print output
print("\n📊 Resume Ranking Based on Job Description:\n")
for i, (name, score) in enumerate(results, 1):
    print(f"{i}. {name} — Match Score: {score:.2f}")
sender_email = "youremail@example.com"
password = "yourpassword"
