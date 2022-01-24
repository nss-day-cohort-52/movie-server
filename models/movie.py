class Movie:
    def __init__(self, id, genre, name, movie_rating, is_showing):
        self.id = id
        self.genre = genre
        self.name = name
        self.movie_rating = movie_rating
        self.is_showing = is_showing
        self.actors = []
