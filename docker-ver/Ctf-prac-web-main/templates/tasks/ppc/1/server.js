// server.js

const express = require('express');
const path = require('path');
const { v4: uuidv4, validate: uuidValidate } = require('uuid'); // Импортируем validate
const http = require('http');
const socketIo = require('socket.io'); // Импортируем socket.io
const app = express();
const port = 3000;

// Создаем HTTP сервер и подключаем socket.io
const server = http.createServer(app);
const io = socketIo(server);

// Флаг хранится на сервере
const FLAG = 'CTF{you_clicked_fast_enough}';

// Middleware для обработки JSON
app.use(express.json());

// Обслуживание статических файлов из папки public
app.use(express.static(path.join(__dirname, 'public')));

// Переменная для хранения данных сессий
let sessions = {};

// Максимальное количество активных сессий
const MAX_SESSIONS = 1000;

// API для получения начальных данных
app.get('/api/init', (req, res) => {
    if (Object.keys(sessions).length >= MAX_SESSIONS) {
        return res.status(503).json({ success: false, message: 'Слишком много активных сессий. Пожалуйста, попробуйте позже.' });
    }

    const clicksRemaining = Math.floor(Math.random() * 501) + 500; // От 500 до 1000
    const sessionId = uuidv4(); // Генерация уникального sessionId

    // Сохраняем данные сессии
    sessions[sessionId] = {
        clicksRemaining,
        startTime: Date.now(),
        clicksPerformed: 0,
        lastClickTime: 0 // Время последнего клика
    };

    res.json({ clicksRemaining, sessionId });
});

// Обработка подключений WebSocket
io.on('connection', (socket) => {
    console.log('Новый клиент подключен');

    socket.on('register', (sessionId) => {
        if (!uuidValidate(sessionId)) {
            socket.emit('errorMessage', 'Неверный формат sessionId');
            return;
        }

        const session = sessions[sessionId];
        if (!session) {
            socket.emit('errorMessage', 'Неверная сессия');
            return;
        }

        socket.sessionId = sessionId;
    });

    socket.on('click', () => {
        const sessionId = socket.sessionId;
        if (!sessionId) {
            socket.emit('errorMessage', 'Сессия не зарегистрирована');
            return;
        }

        const session = sessions[sessionId];
        if (!session) {
            socket.emit('errorMessage', 'Неверная сессия');
            return;
        }

        const timeElapsed = (Date.now() - session.startTime) / 1000;
        if (timeElapsed > 30) {
            delete sessions[sessionId];
            socket.emit('errorMessage', 'Время истекло');
            return;
        }

        const currentTime = Date.now();
        const timeSinceLastClick = currentTime - session.lastClickTime;

        // Проверка минимального интервала между кликами (например, 100 мс)
        const MIN_CLICK_INTERVAL = 100; // в миллисекундах
        if (timeSinceLastClick < MIN_CLICK_INTERVAL) {
            socket.emit('errorMessage', 'Слишком быстрые клики');
            return;
        }

        // Регистрация клика
        session.clicksPerformed += 1;
        session.clicksRemaining -= 1;
        session.lastClickTime = currentTime; // Обновляем время последнего клика

        // Обновляем сессию
        sessions[sessionId] = session;

        // Отправляем обновленное количество кликов
        socket.emit('clickRegistered', { clicksRemaining: session.clicksRemaining });

        // Проверка на окончание кликов
        if (session.clicksRemaining <= 0) {
            socket.emit('flag', { flag: FLAG });
            delete sessions[sessionId];
        }
    });

    socket.on('disconnect', () => {
        console.log('Клиент отключен');
    });
});

// API для проверки прогресса и выдачи флага (если требуется)
app.post('/api/submit', (req, res) => {
    const { sessionId } = req.body;

    // Валидация sessionId
    if (!uuidValidate(sessionId)) {
        return res.json({ success: false, message: 'Неверный формат sessionId' });
    }

    // Проверяем, существует ли сессия
    const session = sessions[sessionId];
    if (!session) {
        return res.json({ success: false, message: 'Неверная сессия' });
    }

    const timeElapsed = (Date.now() - session.startTime) / 1000;

    // Проверяем, что время не истекло
    if (timeElapsed > 30) {
        delete sessions[sessionId];
        return res.json({ success: false, message: 'Время истекло' });
    }

    // Проверяем, что все клики выполнены
    if (session.clicksRemaining > 0) {
        return res.json({ success: false, message: `Необходимо еще ${session.clicksRemaining} кликов` });
    }

    // Выдаем флаг
    delete sessions[sessionId];
    res.json({ success: true, flag: FLAG });
});

// Функция очистки истекших сессий
function cleanExpiredSessions() {
    const now = Date.now();
    for (const [sessionId, session] of Object.entries(sessions)) {
        const timeElapsed = (now - session.startTime) / 1000;
        if (timeElapsed > 30) {
            delete sessions[sessionId];
        }
    }
}

// Запуск очистки каждые 5 минут
setInterval(cleanExpiredSessions, 5 * 60 * 1000);

// Запуск сервера
server.listen(port, () => {
    console.log(`Сервер запущен на http://localhost:${port}`);
});
