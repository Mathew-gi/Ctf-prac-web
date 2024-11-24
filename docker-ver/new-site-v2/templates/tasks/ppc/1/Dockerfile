FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы приложения
COPY package*.json ./
COPY server.js ./
COPY public ./public

# Устанавливаем зависимости
RUN npm install

# Открываем порт
EXPOSE 3000

# Запускаем приложение
CMD ["node", "server.js"]
