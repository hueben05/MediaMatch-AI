# MediaMatch AI

MediaMatch AI is a content-based anime recommendation system I am building to learn machine learning, NLP, data engineering, API development, and recommender-system development.

The long-term goal is to create a personalized anime discovery application that recommends anime based on viewing history, preferences, filters, and natural-language requests.

## Current Pipeline

Raw CSV → Pandas Cleaning → Cleaned CSV → SQLite/SQL → TF-IDF Synopsis Similarity + Genre Similarity → Multi-Anime Taste Profile → Flask REST API → Docker → Render

## What I’ve Built

- Cleaned and prepared an approximately 10,000-row anime dataset using Pandas
- Handled missing values and unnecessary columns
- Stored the cleaned data in SQLite and practiced SQL queries
- Built a Stage 1 content-based recommender using TF-IDF on anime synopses and cosine similarity
- Evaluated the Stage 1 baseline across 5 anime and 25 recommendations, producing a human relevance score of 1.31/5
- Added richer anime metadata and genre similarity in Stage 2
- Combined synopsis similarity at 70% and genre similarity at 30%
- Improved the same benchmark to 3.54/5 in Stage 2
- Built a Stage 3 multi-anime recommendation profile from several liked anime
- Averaged the liked-anime TF-IDF vectors into one combined synopsis taste profile
- Built a weighted genre taste profile from the user’s liked anime
- Prevented selected anime from being recommended back to the user
- Returned structured recommendation data including title, similarity, score, type, and episode count
- Built a Flask REST API with JSON input validation and error handling
- Built a pytest suite with 15 tests covering recommendation logic and Flask API validation
- Containerized the API with Docker
- Deployed the Dockerized API on Render and verified valid and invalid live requests
- Tested a Gunicorn-based Docker startup locally for the public deployment path

## Technologies

- Python
- Pandas
- SQLite
- SQL
- scikit-learn
- TF-IDF
- Cosine Similarity
- Flask
- REST APIs
- pytest
- Docker
- Gunicorn
- Render
- Git / GitHub

## Current Focus

Stage 3 of MediaMatch AI is complete.

The current system builds a taste profile from multiple anime a user likes by combining synopsis TF-IDF similarity with genre similarity. MediaMatch exposes this recommendation system through a tested Flask REST API.

The API has been containerized with Docker and deployed on Render. The Docker startup path has also been tested locally with Gunicorn as the production server.

The next development step is focused PyTorch preparation before Stage 4, where MediaMatch will add pretrained transformer embeddings for semantic recommendation.

## Running MediaMatch

### Local Flask Development

```bash
python3 -m src.app
```

The API runs locally on port 5001 unless a different `PORT` environment variable is provided.

### Docker

Build the image:

```bash
docker build -t mediamatch-ai .
```

Run the container:

```bash
docker run -p 5001:5001 mediamatch-ai
```

Test the recommendation endpoint:

```bash
curl -X POST http://127.0.0.1:5001/recommend \
-H "Content-Type: application/json" \
-d '{"liked_titles":["Naruto","Death Note"]}'
```

### Live Deployment

MediaMatch AI is deployed on Render:

`https://mediamatch-ai.onrender.com`

The recommendation endpoint is:

`POST /recommend`

Example JSON request:

```json
{
  "liked_titles": ["Naruto", "Death Note"]
}
```

## Future Direction

Planned stages include:

- Pretrained transformer embeddings for semantic recommendations
- User-controlled filters for format, rating, episode length, genre, and exclusions
- Stored viewing history, likes, and dislikes for persistent personalization
- Natural-language recommendation requests
- A web interface for browsing, search, filters, and personalized recommendation cards
- Final testing, documentation, evaluation, and recruiter-ready project presentation

The project is being developed incrementally so I can understand, test, and explain each part of the recommendation pipeline before adding more advanced features.
