from utils import extract_text_from_pdf
from nlp_processing import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(resume_pdfs, job_desc):
    processed_resumes = [preprocess_text(extract_text_from_pdf(pdf)) for pdf in resume_pdfs]
    processed_job_desc = preprocess_text(job_desc)

    resume_features, job_features = extract_features(processed_resumes, processed_job_desc)
    scores = cosine_similarity(resume_features, job_features.reshape(1, -1))

    ranked_resumes = sorted(zip(resume_pdfs, scores), key=lambda x: x[1], reverse=True)
    return ranked_resumes
