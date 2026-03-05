from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def search_dataframe(df, query):

    text_data = df.astype(str).apply(lambda x: " ".join(x), axis=1)

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(text_data)

    query_vec = vectorizer.transform([query])

    similarity = cosine_similarity(query_vec, vectors)

    scores = similarity.flatten()

    top_indices = scores.argsort()[-5:][::-1]

    return df.iloc[top_indices]
