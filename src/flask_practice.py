from flask import Flask, request

from recommend import recommend_anime

app = Flask(__name__)

@app.route("/recommend", methods = ["POST"])

def recommend():
    data = request.get_json()
    title = data.get("title") #change this to get all of the titles the user enters
    if title is None:
        return {"error": "Title is required"}, 400
    elif not (isinstance(title, str)) or title.strip() == "":
        return {"error": "Invalid title input"}, 400
    five_recommended = recommend_anime(title) # call recommend_from_likes(liked_titles)
    if five_recommended is None:
        return {"error": "Anime not found"}, 404
    return {"recommendation": five_recommended}

if __name__ == "__main__":
    app.run(debug=True, port = 5001)
