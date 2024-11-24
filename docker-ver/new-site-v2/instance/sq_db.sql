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

CREATE TABLE IF NOT EXISTS TasksPWN (
    id integer PRIMARY KEY AUTOINCREMENT,
    title text NOT NULL,
    difficulty text NOT NULL,
    description text NOT NULL,
    task text NOT NULL,
    solution text NOT NULL
);

INSERT INTO Teams VALUES (NULL, 'CTF-отдел', 0, '00000000');
INSERT INTO Teams VALUES (NULL, 'ФМШ и Челики', 0, '00000000');

INSERT INTO TasksWeb VALUES (NULL, 'Infinity Timer', 'hard', 'description', '/TasksWeb/1', 'limeCTF{tim3_1s_r3lativ3}');

INSERT INTO TasksPPC VALUES (NULL, 'Clicker', 'hard', 'description', '/TasksPPC/1', 'CTF{you_clicked_fast_enough}');

INSERT INTO TasksReverse VALUES (NULL, 'Машина Тайн', 'medium', 'Вы нашли загадочный зашифрованный байткод, который может быть выполнен на виртуальной машине.
Вашей задачей будет расшифровать и проанализировать этот код, чтобы понять его логику и извлечь скрытый флаг.
Формат флага ctf{word_word_word}', '/TasksReverse/1', 'ctf{vm_puzzle_mach1n3}');

INSERT INTO TasksReverse VALUES (NULL, 'Код в движении', 'easy', 'Вы получили файл с загадочными строками. Кажется, что это не просто случайный набор символов. 
После внимательного анализа вы замечаете, что некоторые символы могут представлять собой команды для управления оборудованием. 
Разгадай скрытое значение этих команд, чтобы понять, с чем работает система, и найти ключ, спрятанный в этой сложной головоломке.
Формат флага ctf{word_word}', '/TasksReverse/2', 'ctf{gcode_master}');

INSERT INTO TasksSteganography VALUES (NULL, 'Мозаика Волн', 'medium', 'Звуки этого аудиофайла скрывают тайну, которую можно раскрыть только тем, кто прислушается. Найденное будет ключом к следующему шагу.
Для расшифровки последовательности символов нужна внимательность и немного музыки. Некоторые буквы станут ясны только после правильной расстановки.
C _ _ ? m _ _ _ _ _ ? i _ ? _ _ e ? k _ _ ?
Формат флага Ctf{word_word_word_word}', '/TasksSteganography/1', 'Ctf{melody_is_the_key}');

INSERT INTO TasksCrypto VALUES (NULL, 'Squares', 'easy', 'SQUARES', '/TasksCrypto/1', 'flag{squares}');
-- INSERT INTO TasksPWN VALUES ();
INSERT INTO TasksOSINT VALUES (NULL, 'LOLO', 'easy', 'desc', '/TasksOSINT/1', 'flag{lolo}');

INSERT INTO TasksForensic VALUES (NULL, 'Следы на бумаге', 'medium', 'На фотографии запечатлён загадочный объект с характерным узором. Что это может значить? Твоя задача — выяснить, как извлечь из него скрытое сообщение, и найти флаг.
Формат флага: ctf{WORD}.
Примечание: в флаге используются цифры, а также символы латиницы и кирилицы.', '/TasksForensic/1', 'ctf{Т3ЛEГRАF}');