import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer

# Load cleaned anime data
df = pd.read_csv("data/cleaned/anime_cleaned.csv")

# Turn anime synopses into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")

anime_vectors = vectorizer.fit_transform(df["synopsis"])

from sklearn.metrics.pairwise import cosine_similarity

def title_similarity(title1, title2):
    translator = str.maketrans("", "", string.punctuation)
    new_title1 = title1.translate(translator).lower().split()
    new_title2 = title2.translate(translator).lower().split()
    mySet = set(new_title1)
    mySet2 = set(new_title2)
    shared = mySet.intersection(mySet2)
    unique = mySet.union(mySet2)
    similarity = (len(shared)/len(unique)) * 100
    return similarity

def recommend_anime(title):
    matches = df[df["title"].str.lower() == title.lower()]

    if matches.empty:
        print("Anime not found.")
        return

    anime_index = matches.index[0]

    similarities = cosine_similarity(
        anime_vectors[anime_index],
        anime_vectors
    ).flatten()

    similar_indices = similarities.argsort()[::-1]

    recommendations = []

    for index in similar_indices:
        candidate_title = df.iloc[index]["title"]

        # Skip the anime itself
        if candidate_title.lower() == title.lower():
            continue

        # Skip obvious entries from the same franchise
        if title.lower() in candidate_title.lower():
            continue
        
        if title_similarity(title, candidate_title) >= 30:
            continue

        anime_score = df.iloc[index]["score"]
        anime_type = df.iloc[index]["type"]
        anime_episodes = df.iloc[index]["episodes"]

        recommendation_data = {"title": candidate_title, "similarity": round(similarities[index],3), "score": anime_score, "type": anime_type, "episodes": anime_episodes}


        recommendations.append(recommendation_data)

        if len(recommendations) == 5:
            break

    print(f"\nRecommendations for {title}:")

    for anime_dict in recommendations:
        print(f"Title: {anime_dict["title"]}\nSimilarity: {anime_dict["similarity"]}\nScore: {anime_dict["score"]}\nType: {anime_dict["type"]}\nEpisodes: {anime_dict["episodes"]}\n")
    return recommendations
results = recommend_anime("Naruto")
print(results[0]["title"])
