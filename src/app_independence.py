from flask import Flask, request

from src.recommend import recommend_from_likes

app = Flask(__name__)

@app.route("/recommend", methods = ["POST"])

def recommend():
    data = request.get_json()
    liked_titles = data.get("liked_titles")
    if liked_titles is None:
        return {"response": "missing input"}, 400
    elif not isinstance(liked_titles, list) or liked_titles == []:
        return {"response": "incorrect input"}, 400
    for title in liked_titles:
        if not isinstance(title, str) or title.strip() == "":
            return {"response": "incorrect input"}, 400
    five_recommended = recommend_from_likes(liked_titles)
    if isinstance(five_recommended,str):
        return five_recommended, 404
    return {"recommendation": five_recommended}, 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)