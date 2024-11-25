import os

def solve_task(start_file, base_dir="generated_files"):
    visited = set()
    current_file = start_file

    while True:
        if current_file in visited:
            print(f"Цикл обнаружен! Файл {current_file} уже был посещён.")
            break

        visited.add(current_file)
        file_path = os.path.join(base_dir, current_file)

        if not os.path.exists(file_path):
            print(f"Файл {file_path} не найден!")
            break

        with open(file_path, 'r') as f:
            content = f.read().strip()

        print(f"Читаем {current_file} -> содержимое: {content}")

        if "CTF{" in content or "limeCTF{" in content:
            print(f"Флаг найден: {content}")
            break

        current_file = content

if __name__ == "__main__":
    start_file = "dir1/file1.txt"  # Начальный файл
    solve_task(start_file)
