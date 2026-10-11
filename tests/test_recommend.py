from src.recommend import recommend_anime, title_similarity


def test_similarity():
    similarity = title_similarity("Shingeki no Kyojin", "Shingeki! Kyojin Chuugakkou")
    assert similarity == 50.0

def test_unrelated_titles_have_zero_similarity():
    similarity = title_similarity("Naruto","Death Note")
    assert similarity == 0.0

def test_unknown_titles():
    result = recommend_anime("This Title Does Not Exist")
    assert result is None

def test_original_title():
    result = recommend_anime("Naruto")
    for anime_dict in result:
        assert anime_dict["title"] != "Naruto"

def test_punctuation_capitalization():
    similarity = title_similarity("One Piece!","one piece")
    assert similarity == 100.0

def test_similarity_30_below():
    result = recommend_anime("Shingeki no Kyojin")
    for anime_dict in result:
        similarity = title_similarity("Shingeki no Kyojin", anime_dict["title"])
        assert similarity < 30.0