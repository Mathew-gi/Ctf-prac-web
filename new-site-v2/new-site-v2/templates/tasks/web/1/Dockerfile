# Используем базовый образ Python
FROM python:3.11.3-slim

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем файлы приложения в контейнер
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Указываем порт, на котором будет работать приложение
EXPOSE 5001

# Запускаем приложение
CMD ["python", "app.py"]

