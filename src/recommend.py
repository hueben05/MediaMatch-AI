import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer

# Load cleaned anime data
df = pd.read_csv("data/cleaned/anime_cleaned.csv")

# Turn anime synopses into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")

anime_vectors = vectorizer.fit_transform(df["synopsis"])

from sklearn.metrics.pairwise import cosine_similarity

def clean_title(title):
  for punctuation in string.punctuation:
    title = title.replace(punctuation, " ")
  title = title.lower()
  title = title.split()
  return title

def title_similarity(title1, title2):
    new_title1 = clean_title(title1)
    new_title2 = clean_title(title2)
    mySet = set(new_title1)
    mySet2 = set(new_title2)
    shared = mySet.intersection(mySet2)
    unique = mySet.union(mySet2)
    similarity = (len(shared)/len(unique)) * 100
    return similarity

def recommend_anime(title):
    match_mask = df["title"].str.lower() == title.lower()
    matches = df[match_mask]

    if matches.empty:
        print("Anime not found.")
        return

    anime_index = matches.index[0]

    similarities = cosine_similarity(
        anime_vectors[anime_index],
        anime_vectors
    ).flatten()

    sorted_indices = similarities.argsort()
    similar_indices = sorted_indices[::-1]

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

if __name__ == "__main__":
    results = recommend_anime("Shingeki no Kyojin")
