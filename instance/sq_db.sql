CREATE TABLE IF NOT EXISTS Users (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    password text NOT NULL,
    trueFlags text NOT NULL
);

CREATE TABLE IF NOT EXISTS Points (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    pointValue integer NOT NULL
);

CREATE TABLE IF NOT EXISTS TasksWeb (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);