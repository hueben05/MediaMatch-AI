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
- Added post-processing to reduce same-franchise recommendations
- Added title normalization and Jaccard-style word similarity for title filtering
- Tested recommendations on multiple anime to identify weaknesses and failure cases

## Technologies

- Python
- Pandas
- SQLite
- SQL
- scikit-learn
- TF-IDF
- Cosine Similarity
- Git / GitHub

## Current Focus

The current recommender relies mainly on synopsis text, so recommendation quality can vary when synopsis similarity is low.

I am currently focused on:

- Evaluating recommendation quality
- Improving franchise filtering
- Identifying weaknesses in the baseline model
- Preparing for richer metadata and multi-feature recommendations

## Future Direction

Planned stages include:

- Genre, type, episode count, rating, and other metadata
- Recommendations based on multiple liked anime
- User preference profiles and viewing history
- Filters for mood, length, format, and rating
- Natural-language recommendation requests
- A web interface for browsing and personalized recommendations

The project is being developed incrementally so I can understand and explain each part of the recommendation pipeline before adding more advanced features.