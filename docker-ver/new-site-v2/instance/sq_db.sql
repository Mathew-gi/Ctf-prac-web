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


INSERT INTO Teams VALUES (NULL, 'CTF-отдел', 0, '0000000000000');
INSERT INTO Teams VALUES (NULL, 'ФМШ и Перваки', 0, '0000000000000');

INSERT INTO TasksWeb VALUES (NULL, 'Infinity Timer', 'easy', 'Лаймы в опасности... Давайте спасем их ^-^. Пусть они живут ВЕЧНО
Формат флага limeCTF{word_word_word}
', '/TasksWeb/1', 'limeCTF{tim3_1s_r3lativ3}');

INSERT INTO TasksPPC VALUES (NULL, 'Lime Clicker', 'easy', 'О, это самый обычный кликер. Если выйграешь, то сервер даст тебе flag Ты справишься? Справишься же, да?...
Формат флага limeCTF{word_word_word_word}
', '/TasksPPC/1', 'limeCTF{you_clicked_fast_enough}');

INSERT INTO TasksPPC VALUES (NULL, 'Snake server', 'hard', 'Зря мой товарищ открыл сервер. Сейчас мы быстро узнаем все его секреты... Подключение: ftp 90.156.156.157, креды - ftpuser/ftpuser
Формат флага limeCTF{word_word_word_word_word}
', '/TasksPPC/2', 'limeCTF{who_stores_files_like_that}');

INSERT INTO TasksReverse VALUES (NULL, 'Machine of Mysteries', 'hard', 'Вы нашли загадочный зашифрованный байткод, который может быть выполнен на виртуальной машине.
Вашей задачей будет расшифровать и проанализировать этот код, чтобы понять его логику и извлечь скрытый флаг.
Формат флага limeCTF{word_word_word}
', '/TasksReverse/1', 'limeCTF{vm_puzzle_mach1n3}');

INSERT INTO TasksReverse VALUES (NULL, 'Code in Motion', 'easy', 'Вы получили файл с загадочными строками. Кажется, что это не просто случайный набор символов. 
После внимательного анализа вы замечаете, что некоторые символы могут представлять собой команды для управления оборудованием. 
Разгадай скрытое значение этих команд, чтобы понять, с чем работает система, и найти ключ, спрятанный в этой сложной головоломке.
Формат флага limeCTF{word_word}
', '/TasksReverse/2', 'limeCTF{gcode_master}');

INSERT INTO TasksSteganography VALUES (NULL, 'Mosaic of Waves', 'easy', 'Звуки этого аудиофайла скрывают тайну, которую можно раскрыть только тем, кто прислушается. Найденное будет ключом к следующему шагу.
Для расшифровки последовательности символов нужна внимательность и немного музыки. Некоторые буквы станут ясны только после правильной расстановки.
l _ _ _ C _ _ ? m _ _ _ _ _ ? i _ ? _ _ e ? k _ _ ?
Формат флага limeCTF{word_word_word_word}
', '/TasksSteganography/1', 'limeCTF{melody_is_the_key}');

INSERT INTO TasksSteganography VALUES (NULL, 'M000re parts', 'hard', 'На просторах интернета мне попалось необычное изображение. На первый взгляд, ничего особенного, но интуиция подсказывала, что здесь не всё так просто. Решил покопаться, вдруг получится найти что-то интересное.
В процессе стало ясно, что изображение хранит тайну. Там спрятан флаг, но он разделён на две части. Собрать его целиком — задача не из простых. Это требует внимательности, знаний и подходящих инструментов.
Что ж, теперь твоя очередь попробовать разгадать загадку. Сможешь найти обе части и собрать флаг? Удачи в поисках!
Формат флага limeCTF{word_word_word_word_word}
', '/TasksSteganography/2', 'limeCTF{message_is_hidden_and_encrypted}');

INSERT INTO TasksCrypto VALUES (NULL, 'Colorized Squares', 'easy', 'На днях было скучно, хорошо, что знакомый криптограф подкинул мне "детскую задачку". 
Пообещал дать еще, если справлюсь с этой. В помощь он рассказал, что всего есть девять операций: +, -, *, /, оставить четные, оставить нечетные, инверсировать операцию, ничего не делать, исключить число. 
А также есть массив цифр: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. Название первых двух файлов - и есть значение, которые зашифрованы в них, а значение третьего - ваш флаг.
Интересно, как работают операции? Удачи, в вычислениях флага!
Формат флага limeCTF{0000}
', '/TasksCrypto/1', 'limeCTF{2485}');

INSERT INTO TasksCrypto VALUES (NULL, 'Houston, we have problems', 'hard', 'Вы - шпион и похоже, что у вас проблемы: один хороший знакомый позвонил вам с новостью, что за Вами выехали.
Времени остается мало, пора писать штабу - I was exposed! Что? Шифратор сломался? И как отправить им сообщение? А может получится сбежать?
nc 90.156.156.157 11111
Формат флага limeCTF{word_word_word_word_word_word_word}
', '/TasksCrypto/2', 'limeCTF{1t_15_hard_t0_b3_a_5py}');

INSERT INTO TasksOSINT VALUES (NULL, 'The crime scene', 'easy', 'Мой одноклассник рассказал мне, что некий человек, известный под именем Фанат Лололошки, обнаружил незаконную деятельность в одном месте.
Одноклассник очень боится за свою безопасность, поэтому решил оставить подсказки в интернете, чтобы помочь разобраться в ситуации, если с ним что-то случится.', '/TasksOSINT/1', 'limeCTF{Pushka}');

INSERT INTO TasksOSINT VALUES (NULL, 'Telegram channels', 'hard', 'Все находится в документ.txt', '/TasksOSINT/2', 'limeCTF(Crazy_telegram}');

INSERT INTO TasksForensic VALUES (NULL, 'Traces on Paper', 'hard', 'На фотографии запечатлён загадочный объект с характерным узором. Что это может значить? Твоя задача — выяснить, как извлечь из него скрытое сообщение, и найти флаг.
Формат флага: limeCTF{WORD}.
Примечание: в флаге используются цифры, а также символы латиницы и кирилицы.', '/TasksForensic/1', 'limeCTF{Т3ЛEГРАФ}');

INSERT INTO TasksForensic VALUES (NULL, 'Secret in the Headers', 'easy', 'Вы перехватили сетевой трафик, в котором содержится важная информация, скрытая в HTTP-запросе.
Секрет зашифрован в одном из стандартных заголовков, который на первый взгляд может показаться обычным. 
Однако, если внимательно его изучить, можно заметить, что часть данных закодирована. Ваша задача — найти и декодировать эту скрытую информацию, чтобы получить флаг.
Формат флага: limeCTF{WORD_Word_Word_Word}.', '/TasksForensic/2', 'limeCTF{HTTP_U5er_Agent_R3v3aled}');
