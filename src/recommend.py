import string

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load cleaned anime data
df = pd.read_csv("data/cleaned/anime_with_metadata.csv")

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

def genre_similarity(genres1, genres2):
    if pd.isna(genres1) or pd.isna(genres2):
        return 0
    genres1 = {genre.strip().lower() for genre in genres1.split(",")}  
    genres2 = {genre.strip().lower() for genre in genres2.split(",")}  
    shared = genres1.intersection(genres2)
    unique = genres1.union(genres2)
    similarity = len(shared) / len(unique)
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

    searched_genres = df.iloc[anime_index]["genres"]
    combined_scores = []

    for index in range(len(df)):
        anime_genres = df.iloc[index]["genres"]
        anime_genre_similarity = genre_similarity(anime_genres,searched_genres)
        combined_similarity = (similarities[index] * .70) + (anime_genre_similarity * .30)
        combined_scores.append(combined_similarity)

    sorted_indices = pd.Series(combined_scores).argsort()
    similar_indices = sorted_indices[::-1]

    recommendations = []

    for index in similar_indices:
        eng_title = df.iloc[index]["titleEn"]
        candidate_title = df.iloc[index]["title"]
        if pd.isna(eng_title):
            display_title = candidate_title
        else:
            display_title = eng_title

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

        recommendation_data = {"title": display_title, "similarity": round(combined_scores[index],3), "score": anime_score, "type": anime_type, "episodes": anime_episodes}


        recommendations.append(recommendation_data)

        if len(recommendations) == 5:
            break

    print(f"\nRecommendations for {title}:")

    for anime_dict in recommendations:
        print(f"Title: {anime_dict["title"]}\nSimilarity: {anime_dict["similarity"]}\nScore: {anime_dict["score"]}\nType: {anime_dict["type"]}\nEpisodes: {anime_dict["episodes"]}\n")
    return recommendations

if __name__ == "__main__":
    results = recommend_anime("Naruto")
    results = recommend_anime("Bleach")
    results = recommend_anime("Death Note")
    results = recommend_anime("One Piece")
    results = recommend_anime("Shingeki no Kyojin")
