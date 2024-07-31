import numpy as np 
import pandas as pd 

from sklearn.metrics .pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def cosine(query_embedded, database_embeded):
    return cosine_similarity(query_embedded.reshape(1,-1), database_embeded)


def tfidf_search (question , tfidf_vectorizer : TfidfVectorizer,context_embedded, top_d =5):

    query_embedded = [doc.lower() for doc in [question]]
    query_embedded = tfidf_vectorizer.transform(query_embedded)
    query_embedded = query_embedded.toarray().reshape(-1)
    cosine_scores = cosine(query_embedded,context_embedded)[0]

    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][:: -1]:
        doc_score = {
            "id": idx ,
            "cosine_score": cosine_scores[idx], 
        }
        results.append(doc_score )
    return results

if __name__ == "__main__" :

    vi_data_df = pd.read_csv ("vi_text_retrieval.csv")
    context = vi_data_df ["text"]
    context = [doc.lower () for doc in context]

    tfidf_vectorizer = TfidfVectorizer ()
    context_embedded = tfidf_vectorizer.fit_transform(context)

    question = vi_data_df.iloc[0]["question"]
    print(f'Question: {question}')
    
    results = tfidf_search (question, tfidf_vectorizer, context_embedded ,top_d =5)
    print(results[0]["cosine_score"])