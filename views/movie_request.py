import sqlite3

import json
from models.movie import Movie
from models.actor import Actor


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

            db_cursor.execute("""
                select a.id, a.name
                from Movie_actor ma
                join Actors a on a.id = ma.actor_id
                where ma.movie_id = ?
            """, (movie.id, ))

            actors = []

            actor_dataset = db_cursor.fetchall()

            for actor_row in actor_dataset:
                actor = Actor(actor_row['id'], actor_row['name'])
                actors.append(actor.__dict__)

            movie.actors = actors

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


def create_movie(movie):
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        insert into Movies (genre, name, is_showing, movie_rating ) 
        values (?, ?, ?, ?)
        """, (movie['genre'], movie['name'], movie['is_showing'], movie['movie_rating'], ))

        id = db_cursor.lastrowid

        movie['id'] = id

        for actor_id in movie['actors']:
            db_cursor.execute("""
                insert into Movie_Actor values (null, ?, ?)
            """, (actor_id, movie['id']))

        return json.dumps(movie)
