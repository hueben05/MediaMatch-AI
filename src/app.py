from flask import Flask, request

from src.recommend import recommend_from_likes

app = Flask(__name__)

@app.route("/recommend", methods = ["POST"])

def recommend():
    data = request.get_json(silent=True)
    if not isinstance(data,dict):
        return {"error": "Invalid JSON input"}, 400
    liked_titles = data.get("liked_titles") 
    if liked_titles is None: 
        return {"error": "Title is required"}, 400
    elif not (isinstance(liked_titles, list)) or liked_titles == []:
        return {"error": "Invalid title input"}, 400
    for title in liked_titles:
        if not (isinstance(title, str)) or title.strip() == "":
            return {"error": "Invalid title input"}, 400
    five_recommended = recommend_from_likes(liked_titles) 
    if isinstance(five_recommended, str):
        return {"error": "Anime not found"}, 404
    return {"recommendation": five_recommended}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port = 5001)
