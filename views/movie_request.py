import sqlite3

import json
from models.movie import Movie

def get_all_movies():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select * from Movies
        """)

        movies = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            movie = Movie(row['id'], row['genre'], row['name'],
                          row['movie_rating'], row['is_showing'])
            movies.append(movie.__dict__)
        
    return json.dumps(movies)


def get_single_movie(id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select * from Movies
        where id = ?
        """, (id, ))

        row = db_cursor.fetchone()

        movie = Movie(row['id'], row['genre'], row['name'],
                          row['movie_rating'], row['is_showing'])

        return json.dumps(movie.__dict__)


