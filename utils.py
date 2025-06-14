# utils.py
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def get_resume_scores(job_description, resumes_folder):
    resumes = []
    resume_names = []
    
    for file in os.listdir(resumes_folder):
        if file.endswith('.txt'):
            path = os.path.join(resumes_folder, file)
            resumes.append(read_file(path))
            resume_names.append(file)
    
    documents = [job_description] + resumes
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    
    job_vector = vectors[0:1]
    resume_vectors = vectors[1:]
    
    similarities = cosine_similarity(job_vector, resume_vectors)[0]
    return list(zip(resume_names, similarities))
