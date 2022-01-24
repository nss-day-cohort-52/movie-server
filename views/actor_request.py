import json
import sqlite3

from models.actor import Actor


def get_all_actors():
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select * from Actors
        """)

        actors = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            actor = Actor(row['id'], row['name'])
            actors.append(actor.__dict__)
        
    return json.dumps(actors)


def get_single_actor(id):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select * from Actors
        where id = ?
        """, (id, ))

        row = db_cursor.fetchone()

        actor = Actor(row['id'], row['name'])

        return json.dumps(actor.__dict__)
