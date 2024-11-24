# Ctf-prac-web

***
## Категория WEB
### ?
#### Описание
#### Подсказка
#### Решение
### ?
#### Описание
#### Подсказка
#### Решение

***
## Категория REVERSE
### Lime Clicker
#### Описание
#### Подсказка
#### Решение
### ?
#### Описание
#### Подсказка
#### Решение

***
## Категория CRYPTO
### Colorized Squares
#### Описание
На днях было скучно, хорошо, что знакомый криптограф подкинул мне "детскую задачку". Пообещал дать еще, если справлюсь с этой.
В помощь он рассказал, что всего есть девять операций: +, -, *, /, оставить четные, оставить нечетные, инверсировать операцию, ничего не делать, исключить число. А также есть массив цифр: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
Название первых двух файлов - и есть значение, которые зашифрованы в них, а значение третьего - ваш флаг. Интересно, как работают операции? Удачи, в вычислениях флага!
#### Подсказка
Сопоставив квадраты и значения, которые они представляют, можно догадаться, что каждый из цветов: красный, оранжевый, желтый, зеленый, голубой, синий, фиолетовый, черный и белый - какая-то операция из данных.
При том, операции выполняются спиралью по часовой. Какие-то операции берут все числа из массива, а какие-то оперируют уже найденное число на исключенное справа.
#### Решение
Расшифровка цветов:
| Цвет       | К  | О                    | Ж  | З  | Г                    | С  | Ф  | Ч                      | Б                 |
|------------|----|----------------------|----|----|----------------------|----|----|------------------------|-------------------|
| Операция   | +  | Оставить четные      | *  | /  | Оставить нечетные    | -  | ^  | Инверсировать операцию | Ничего не делать  |
Цифра в верхнем левом углу квадрата, при наличии, исключает данную цифру из набора.
Операции +, -, оставить четные, оставить нечетные, инверсировать операция, ничего не делать - применяется ко всему набору.
Операции *, /, ^ - берут текущее выражение и оперируют на исключенное число справа
Рамка, окружающаю квдрат - применяет операцию к текущему выражению, а не к набору
Выражение всегда округляется до целого большего

Разбор задания:
1. Исключаем из набора 2: [1, 3, 4, 5, 6, 7, 8, 9]
2. Отбираем четные из набора: [4, 6, 8]
3. Применяем к набору -: 4 - 6 - 8 = -10
4. Применяем к выражению ^: -10 ^ 2 = 100
5. Ничего не делаем с выражением: 100
6. Применяем к выражениям сложение: 100 + (
7. Отбираем четные из набора: [4, 6, 8]
8. Применяем к набору +: 4 + 6 + 8 = 18
9. Применяем к выражению *: 18 * 2 = 36
10. Инверсируем последнюю операцию: 18 / 2 = 9
11. Применяем к выражениям умножение: 100 + (9 * (
12. Отбираем нечетные из набора: [1, 3, 5, 7, 9]
13. Применяем к набору -: 1 - 3 - 5 - 7 - 9 = -23
14. Применяем к выражению ^: -23 ^ 2 = 529
15. Применяем к выражению /: 529 // 2 = 265
16. Вычисляем конечное выражение: 100 + (9 * (265)) = 2485
##### Ответ: limeCTF{2485}
### ?
#### Описание
#### Подсказка
#### Решение

***
## Категория OSINT
### The crime scene
#### Описание
Мой одноклассник рассказал мне, что некий человек, известный под именем Фанат Лололошки, обнаружил незаконную деятельность в одном месте. Одноклассник очень боится за свою безопасность, поэтому решил оставить подсказки в интернете, чтобы помочь разобраться в ситуации, если с ним что-то случится.
#### Подсказка 
Внимательно изучите сайт Фаната Лололошки
#### Решение
Исходная информация: Участники начинают с имени: Фанат Лололошки.

Поиск в социальных сетях:

Участники начинают поиск по этому имени в популярных социальных сетях. В результате обнаруживается профиль в Одноклассниках, связанный с этим именем.
На странице профиля участники находят ссылку на личный сайт Фаната Лололошки.

Анализ сайта:
При переходе на сайт становится ясно, что он содержит больше подсказок. Из опубликованной информации видно, что Фанат Лололошки родом из города Уяр.
Также на сайте указано, что Фанат упоминал, что собирался посетить суши-ресторан в своем родном городе.
Географический поиск:

Участники исследуют карты города Уяр (например, через Google Maps или 2ГИС) и находят название единственного суши-ресторана. Это и есть кодовое название места, которое имел в виду мой одноклассник.
limeCTF{Pushka}
### ?
#### Описание
Все находится в документ.txt
#### Подсказка
#### Решение
Анализ начального документа
Участники изучают предоставленный текстовый файл. Основная задача на этом этапе — выявить три Telegram-канала, указанные в документе.
Подсказка: Каналы могут быть замаскированы под ссылки, имена пользователей или упомянуты текстом.

Поиск "Флага Флаговича"
В одном из трёх каналов необходимо найти посты, связанные с "Флагом Флаговичем". Этот персонаж является ключевой фигурой задания.
Важно: Посты могут быть спрятаны среди других сообщений, поэтому участники должны внимательно проверять каждый канал.

Взаимодействие с "Флагом Флаговичем"
Найдя посты, участники переходят на страницу "Флага Флаговича". В описании профиля указано, что нужно написать ему в личные сообщения, чтобы продвинуться дальше.
При отправке сообщения "Флаг Флагович" запрашивает у участника кодовую фразу.

Поиск кодовой фразы
Кодовая фраза спрятана в начальном текстовом документе. Участникам нужно прочитать документ внимательно или использовать поиск по ключевым словам.
Пример: "Введите кодовую фразу: 'Решение кроется в деталях'".

Получение доступа к личному каналу
После предоставления правильной кодовой фразы "Флаг Флагович" отправляет ссылку на закрытый Telegram-канал.

Анализ личного канала
В личном канале содержится ссылка на видеоканал на Rutube. Участникам нужно найти эту ссылку среди сообщений канала.
Подсказка: Ссылка может быть замаскирована или представлена в необычном формате (например, как часть текста или изображения).

Поиск флага на Rutube
На Rutube-канале размещено шесть видео. Участникам нужно просмотреть их и найти то, в котором содержится флаг.

***
## Категория STEGO
### Lime Clicker
#### Описание
#### Подсказка
#### Решение
### M000re parts
#### Описание
На просторах интернета мне попалось необычное изображение. На первый взгляд, ничего особенного, но интуиция подсказывала, что здесь не всё так просто. Решил покопаться, вдруг получится найти что-то интересное.

В процессе стало ясно, что изображение хранит тайну. Там спрятан флаг, но он разделён на две части. Собрать его целиком — задача не из простых. Это требует внимательности, знаний и подходящих инструментов.

Что ж, теперь твоя очередь попробовать разгадать загадку. Сможешь найти обе части и собрать флаг? Удачи в поисках!
#### Подсказка
Красный цвет таит в себе секреты!
#### Решение
Шаг 1: Извлечь первую часть флага (альфа-канал)
Первая часть флага спрятана в младших битах альфа-канала. Используйте следующий код на Python для извлечения:
```
from PIL import Image

image = Image.open("stego_challenge_ctf.png")
pixels = image.load()

width, height = image.size
binary_message = ""

for y in range(height):
    for x in range(width):
        _, _, _, a = pixels[x, y]
        binary_message += str(a & 1)
        # Останавливаем, если достигли конца сообщения
        if len(binary_message) % 8 == 0 and binary_message[-8:] == "00000000":
            break
    else:
        continue
    break

message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message) - 8, 8))
print("Первая часть флага:", message)
```
Результат: limeCTF{message_is_

Шаг 2: Извлечь вторую часть флага (LSB красного канала)
Вторая часть флага спрятана в младших битах красного канала. Используйте следующий код:
```
binary_message = ""

# Извлекаем младшие биты из красного канала
for y in range(height):
    for x in range(width):
        r, _, _, _ = pixels[x, y]
        binary_message += str(r & 1)
        # Останавливаем, если достигли конца сообщения
        if len(binary_message) % 8 == 0 and binary_message[-8:] == "00000000":
            break
    else:
        continue
    break

# Конвертируем из бинарного в текст
message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message) - 8, 8))
print("Вторая часть флага:", message)
```
Результат: hidden_and_encrypted}

Объединяем: limeCTF{message_is_hidden_and_encrypted}
***
## Категория PPC
### Lime Clicker
#### Описание
#### Подсказка
#### Решение
### ?
#### Описание
#### Подсказка
#### Решение

***
## Категория FORENSIC
### Lime Clicker
#### Описание
#### Подсказка
#### Решение
### ?
#### Описание
#### Подсказка
#### Решение

***
## Категория PWN
### Lime Clicker
#### Описание
#### Подсказка
#### Решение
### ?
#### Описание
#### Подсказка
#### Решение
