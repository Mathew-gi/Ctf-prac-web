import os

def solve_task(start_file, base_dir="generated_files"):
    visited = set()  # Чтобы избежать зацикливания
    current_file = start_file

    while True:
        # Проверяем, посещался ли уже файл
        if current_file in visited:
            print(f"Цикл обнаружен! Файл {current_file} уже был посещён.")
            break

        visited.add(current_file)
        file_path = os.path.join(base_dir, current_file)

        # Проверяем существование файла
        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден!")
            break

        try:
            with open(file_path, 'r') as f:
                content = f.read().strip()
        except Exception as e:
            print(f"Ошибка чтения файла {file_path}: {e}")
            break

        # Вывод отладочной информации
        print(f"Читаем {current_file} -> содержимое: {content}")

        # Проверяем, содержит ли файл флаг
        if "CTF{" in content:
            print(f"Флаг найден: {content}")
            break

        # Переходим к следующему файлу
        current_file = content

if __name__ == "__main__":
    # Укажите путь к начальному файлу
    start_file = "dir1/file1.txt"  # Убедитесь, что файл существует
    solve_task(start_file)
