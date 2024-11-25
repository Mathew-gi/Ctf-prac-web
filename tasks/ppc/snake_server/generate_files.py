import os
import random

def create_directories_and_files(num_dirs=100, num_files=10, flag="limeCTF{who_stores_files_like_that}"):
    base_dir = "generated_files"
    os.makedirs(base_dir, exist_ok=True)

    all_files = []
    special_file_name = None  # Инициализируем переменную
    special_file_path = None

    for dir_index in range(1, num_dirs + 1):
        dir_path = f"{base_dir}/dir{dir_index}"
        os.makedirs(dir_path, exist_ok=True)
        for file_index in range(1, num_files + 1):
            # Проверяем, является ли текущий файл тем, который нужно заменить на специальный
            if dir_index == 7 and file_index == 4:
                special_file_name = "fileaXRfaXNfc29fbDAwMG5nX3NuYWtl.txt"
                file_name = special_file_name
                special_file_path = f"dir{dir_index}/{file_name}"
                all_files.append(special_file_path)  # Добавляем специальный файл в список
            else:
                file_name = f"file{file_index}.txt"
                file_path = f"dir{dir_index}/{file_name}"
                all_files.append(file_path)

    # Создаем единую цепочку файлов
    random.shuffle(all_files)
    for i in range(len(all_files) - 1):
        current_file = all_files[i]
        next_file = all_files[i + 1]
        file_path = os.path.join(base_dir, current_file)
        with open(file_path, 'w') as f:
            f.write(next_file)

    # Последний файл содержит флаг
    last_file = all_files[-1]
    file_path = os.path.join(base_dir, last_file)
    with open(file_path, 'w') as f:
        f.write(flag)

    # Выводим информацию о специальном файле
    print(f"Специальный файл находится в: {special_file_path}")
    print(f"Флаг находится в файле: {last_file}")

if __name__ == "__main__":
    create_directories_and_files()
