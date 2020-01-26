from dataclasses import asdict


def find_information_about_movie(movies_list: list, value: str, key: str = "title"):
    """
    finds information about movie in movies list
    :param movies_list: list of UniqueMovie objects
    :param value: value to search
    :param key: can be field which specified in UniqueMovie, default: "title"
    :return: UniqueMovie object (first movie which match key and value)
    """
    for movie in movies_list:
        for movie_key, movie_value in asdict(movie).items():
            if movie_key == key and movie_value == value:
                return movie
    return None
