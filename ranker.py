from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(jd_text, resumes_text_dict):
    documents = [jd_text] + list(resumes_text_dict.values())
    names = list(resumes_text_dict.keys())

    tfidf = TfidfVectorizer().fit_transform(documents)
    similarity_scores = cosine_similarity(tfidf[0:1], tfidf[1:]).flatten()

    ranked = dict(sorted(zip(names, similarity_scores), key=lambda x: x[1], reverse=True))
    return ranked