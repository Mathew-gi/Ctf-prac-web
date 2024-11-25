import socket

# Функция для поиска исходного слова, которое после шифрования даст целевое слово
def find_input_word(target_word):
    encrypted_ascii = [ord(c) for c in target_word]
    length = len(target_word)
    if length % 2 == 1:
        # Для нечётной длины: shift = max(original_ascii_values)
        for shift in range(1, 127):
            original_ascii = [(val - shift) % 127 for val in encrypted_ascii]
            if max(original_ascii) != shift:
                continue
            original_word = ''.join(chr(val) for val in original_ascii)
            # Проверяем допустимость символов
            if all(0 <= ord(c) <= 126 for c in original_word):
                if encoder(original_word) == target_word:
                    return original_word
    else:
        # Для чётной длины: shift = min(original_ascii_values) // 2
        for shift in range(1, 64):
            original_ascii = [(val - shift) % 127 for val in encrypted_ascii]
            min_original_ascii = min(original_ascii)
            if shift != min_original_ascii // 2:
                continue
            original_word = ''.join(chr(val) for val in original_ascii)
            # Проверяем допустимость символов
            if all(0 <= ord(c) <= 126 for c in original_word):
                if encoder(original_word) == target_word:
                    return original_word
    return None

# Функция шифрования для проверки
def encoder(input_string):
    ascii_values = [ord(char) for char in input_string]
    if len(ascii_values) % 2 == 0:
        shift = min(ascii_values) // 2
    else:
        shift = max(ascii_values)
    shifted_ascii = [(value + shift) % 127 for value in ascii_values]
    encoded_string = ''.join(chr(value) for value in shifted_ascii)
    return encoded_string

# Главная функция
def main():
    # Целевое сообщение
    target_message = "I was exposed" # для получение пасхалки замените на "Escape"
    target_words = target_message.split()
    input_messages = []

    # Находим входные слова для каждого целевого слова
    for word in target_words:
        original_word = find_input_word(word)
        if original_word:
            input_messages.append(original_word)
        else:
            print(f"Не удалось найти исходное слово для '{word}'")
            return
            
    # Вывод отсылаемых на сервер сообщений
    print(input_messages)

    # Подключаемся к серверу
    HOST = '127.0.0.1'  # Замените на адрес сервера
    PORT = 11111        # Замените на порт сервера

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Получаем приветственное сообщение и таблицу символов
        data = s.recv(4096).decode('utf-8')
        print(data)

        # Ждём запроса на ввод количества сообщений
        data = s.recv(4096).decode('utf-8')
        print(data)

        # Отправляем количество сообщений
        s.sendall(f"{len(input_messages)}\n".encode('utf-8'))

        # Обрабатываем каждый запрос на ввод сообщения
        for idx in range(len(input_messages)):
            # Ждём запроса на ввод сообщения
            data = s.recv(4096).decode('utf-8')
            print(data)

            # Отправляем сообщение
            msg = input_messages[idx]
            s.sendall(f"{msg}\n".encode('latin1'))

        # Получаем итоговое сообщение и флаг
        while True:
            data = s.recv(4096).decode('utf-8')
            if not data:
                break
            print(data)
            if "limeCTF{" in data or "пасхалк" in data or "Пасхалк" in data:
                break

        # Закрываем соединение
        s.close()

if __name__ == "__main__":
    main()
