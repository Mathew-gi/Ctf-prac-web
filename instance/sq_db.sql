CREATE TABLE IF NOT EXISTS Users (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    password text NOT NULL,
    trueFlags text NOT NULL,
    team text NOT NULL
);

CREATE TABLE IF NOT EXISTS Points (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    pointValue integer NOT NULL
);

CREATE TABLE IF NOT EXISTS Teams (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    pointValue integer NOT NULL,
    trueFlags text NOT NULL
);

CREATE TABLE IF NOT EXISTS TasksWeb (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);

CREATE TABLE IF NOT EXISTS TasksForensic (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);

CREATE TABLE IF NOT EXISTS TasksCrypto (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);

CREATE TABLE IF NOT EXISTS TasksReverse (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);


CREATE TABLE IF NOT EXISTS TasksOSINT (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);


CREATE TABLE IF NOT EXISTS TasksSteganography (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);


CREATE TABLE IF NOT EXISTS TasksPPC (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);


CREATE TABLE IF NOT EXISTS TasksMisc (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);


CREATE TABLE IF NOT EXISTS TasksPWN (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);