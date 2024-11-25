import ftplib
import io

def solve_ftp_task(host, port, username, password, start_file):
    ftp = ftplib.FTP()
    ftp.connect(host, port)
    ftp.login(username, password)
    
    current_file = start_file
    visited = set()
    
    while True:
        # Проверяем, посещался ли уже файл
        if current_file in visited:
            print(f"Цикл обнаружен! Файл {current_file} уже был посещён.")
            break
        visited.add(current_file)
        
        try:
            # Переподключаемся каждый раз
            ftp = ftplib.FTP()
            ftp.connect(host, port)
            ftp.login(username, password)
            
            # Скачиваем файл в память
            r = io.BytesIO()
            ftp.retrbinary(f"RETR {current_file}", r.write)
            content = r.getvalue().decode('utf-8').strip()
            ftp.quit()  # Закрываем соединение сразу после скачивания
        except ftplib.all_errors as e:
            print(f"Ошибка при работе с FTP: {e}")
            break
        
        print(f"Скачали {current_file} -> содержимое: {content}")
        
        # Проверяем, содержит ли файл флаг
        if "CTF{" in content or "limeCTF{" in content:
            print(f"Флаг найден: {content}")
            break
        
        current_file = content  # Переходим к следующему файлу

if __name__ == "__main__":
    host = "127.0.0.1"  # IP-адрес вашего FTP-сервера
    port = 21  # Порт FTP-сервера
    username = "ftpuser"  # Логин FTP-пользователя
    password = "ftpuser"  # Пароль FTP-пользователя
    start_file = "ftp_root/dir1/file1.txt"  # Начальный файл

    solve_ftp_task(host, port, username, password, start_file)

