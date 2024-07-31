import numpy as np 
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer

def calculate_correlations(vector, matrix):
    """
        Correlation cofficient between vector and matrix, result -> vector        
    """
    vector_mean = np.mean(vector)
    matrix_mean = np.mean(matrix, axis=1)
    
    vector_centered = vector - vector_mean
    matrix_centered = matrix - matrix_mean[:, None]
    
    dot_products = np.dot(matrix_centered, vector_centered)
    
    vector_norm = np.linalg.norm(vector_centered)
    matrix_norms = np.linalg.norm(matrix_centered, axis=1)
    
    correlation_coefficients = dot_products / (vector_norm * matrix_norms)
    
    return correlation_coefficients

def corr_search ( question , tfidf_vectorizer:TfidfVectorizer , context_embedded,top_d =5) :

    query_embedded = [doc.lower() for doc in [question]]
    query_embedded = tfidf_vectorizer.transform(query_embedded)
    query_embeded = query_embedded.toarray().reshape(-1)

    corr_scores = calculate_correlations(query_embeded,context_embedded)
    results = []
    for idx in corr_scores.argsort()[-top_d :][:: -1]:
        doc = {
        "id": idx ,
        "corr_score": corr_scores[idx]
        }
    results.append(doc)
    return results  

if __name__ == "__main__":
    vi_data_df = pd.read_csv ("vi_text_retrieval.csv")
    context = vi_data_df ["text"]
    context = [doc.lower () for doc in context]

    tfidf_vectorizer = TfidfVectorizer ()
    context_embedded = tfidf_vectorizer.fit_transform(context)
    context_embedded = context_embedded.toarray()
    question = vi_data_df.iloc[0]["question"]

    print(f"Question: {question}")

    results = corr_search(question , tfidf_vectorizer ,context_embedded, top_d =5)
    print(results [0]["corr_score"])

