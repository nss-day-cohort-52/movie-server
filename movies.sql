create table Actors (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

create table Movies (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    genre TEXT NOT NULL,
    name TEXT NOT NULL,
    movie_rating TEXT NOT NULL,
    is_showing bit NOT NULL
);

create table Movie_Actor (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    actor_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    FOREIGN KEY (actor_id) REFERENCES Actors(id),
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

INSERT INTO Actors values (null, "Angelina Jolie");
INSERT INTO Movies values (null, "Action", "Mr and Mrs Smith", "R", 0);

INSERT INTO Movie_Actor values (null, 1, 1);
