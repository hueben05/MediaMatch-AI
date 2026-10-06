# MediaMatch AI

MediaMatch AI is a content-based anime recommendation system I am building to learn machine learning, NLP, data engineering, and recommender-system development.

The long-term goal is to create a personalized anime discovery application that recommends anime based on viewing history, preferences, filters, and natural-language requests.

## Current Pipeline

Raw CSV → Pandas Cleaning → Cleaned CSV → SQLite/SQL → TF-IDF → Cosine Similarity → Recommendation Filtering

## What I’ve Built

- Cleaned and prepared an approximately 10,000-row anime dataset using Pandas
- Handled missing values and unnecessary columns
- Stored the cleaned data in SQLite and practiced SQL queries
- Built a content-based recommendation system using TF-IDF on anime synopses
- Used cosine similarity to rank similar anime
- Added filtering to prevent the exact searched anime from recommending itself
- Added basic same-franchise filtering
- Added title cleaning and Jaccard-style word similarity for title filtering
- Returned structured recommendation data including title, similarity, score, type, and episode count
- Built a pytest suite with 6 tests covering title similarity, unknown titles, self-recommendations, punctuation/capitalization, and franchise filtering
- Evaluated the baseline recommender across 5 anime and 25 recommendations
- Established a baseline human relevance score of 1.31/5 for future comparison
- Identified weaknesses including shared character names, shallow synopsis overlap, and same-franchise titles with unrelated names
- Refactored repeated and confusing code while keeping all tests passing

## Technologies

- Python
- Pandas
- SQLite
- SQL
- scikit-learn
- TF-IDF
- Cosine Similarity
- pytest
- Git / GitHub

## Current Focus

Stage 1 of the recommendation system is complete.

The current recommender relies primarily on TF-IDF similarity between anime synopses. The baseline evaluation showed that synopsis similarity alone does not consistently capture genre, tone, franchise relationships, or broader viewer preferences.

I am currently focused on improving the recommendation system with richer anime information by:

- Adding genre information to the dataset
- Deciding which fields should affect recommendation similarity and which should act as filters
- Adding genre information to the recommendation process
- Using type, rating, and episode count appropriately
- Comparing the improved recommender against the Stage 1 baseline
- Expanding tests as recommendation behavior becomes more complex

## Future Direction

Planned stages include:

- Recommendations based on multiple liked anime
- User preference profiles and viewing history
- Filters for mood, length, format, genre, and rating
- Natural-language recommendation requests
- Semantic search and embeddings
- A web interface for browsing and personalized recommendations

The project is being developed incrementally so I can understand, test, and explain each part of the recommendation pipeline before adding more advanced features.