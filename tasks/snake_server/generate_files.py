import os
import random
import base64

# Путь к корневой директории FTP
base_dir = "/home/ftpuser/ftp_root"

# Параметры генерации
num_dirs = 100  # Количество директорий
max_files_per_dir = 10  # Максимальное число файлов в одной директории
main_flag = "CTF{main_flag_here}"  # Основной флаг
normal_content = "Следуй к {}"  # Обычное содержимое файлов
file_references = {}  # Карта переходов

# Генерация директорий и файлов
os.makedirs(base_dir, exist_ok=True)

# Создаём все директории и файлы
all_files = []
for i in range(1, num_dirs + 1):
    dir_path = os.path.join(base_dir, f"dir{i}")
    os.makedirs(dir_path, exist_ok=True)
    num_files = random.randint(1, max_files_per_dir)
    for j in range(1, num_files + 1):
        file_path = os.path.join(dir_path, f"file{j}.txt")
        all_files.append(file_path)

# Выбираем файл с флагом
main_flag_file = random.choice(all_files[len(all_files) // 3 : 2 * len(all_files) // 3])  # Ближе к середине

# Генерация путей: файлы указывают друг на друга случайным образом
for file_path in all_files:
    if file_path == main_flag_file:
        file_references[file_path] = main_flag  # Этот файл содержит флаг
    else:
        target_file = random.choice(all_files)
        while target_file == file_path:  # Исключаем самопереходы
            target_file = random.choice(all_files)
        file_references[file_path] = target_file

# Генерация файла с пасхалкой
hidden_dir = os.path.join(base_dir, f"dir50")
hidden_file_name = base64.b64encode(b"hope_you_find_this").decode() + ".txt"
hidden_file_path = os.path.join(hidden_dir, hidden_file_name)
os.makedirs(hidden_dir, exist_ok=True)
file_references[hidden_file_path] = random.choice(all_files)  # Пасхалка указывает на случайный файл

# Записываем содержимое файлов
for file_path, content in file_references.items():
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as f:
        if content == main_flag:
            f.write(main_flag)  # Файл с флагом
        else:
            f.write(normal_content.format(os.path.relpath(content, base_dir)))  # Указываем путь к следующему файлу

print(f"Флаг находится в файле: {main_flag_file}")
print(f"Пасхалка создана: {hidden_file_path}")
