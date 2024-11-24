// script.js

let clicksRemaining;
let timerInterval;
let countdown = 60;
let activeButton = 'left'; // Начинаем с левой кнопки
let sessionId;

const clicksDisplay = document.getElementById('clicksRemaining');
let timerDisplay = document.getElementById('timer'); // Изменено на let
const topArea = document.getElementById('top');
const leftButton = document.getElementById('left');
const rightButton = document.getElementById('right');
const container = document.getElementById('container');
const bottomArea = document.getElementById('bottom'); // Добавлено для доступа к секции таймера

// Подключение к WebSocket серверу
const socket = io();

// Функция для отображения сообщений об ошибках
function displayError(message) {
    const errorMessage = document.createElement('div');
    errorMessage.classList.add('error-message');
    errorMessage.textContent = `Ошибка: ${message}`;
    container.appendChild(errorMessage);

    // Автоматически удалять сообщение через 5 секунд
    setTimeout(() => {
        errorMessage.remove();
    }, 5000);
}

// Обработка ошибок от сервера
socket.on('errorMessage', (message) => {
    displayError(message);
});

// Обработка регистрации клика
socket.on('clickRegistered', (data) => {
    clicksRemaining = data.clicksRemaining;
    clicksDisplay.textContent = clicksRemaining;
    console.log(`Клик зарегистрирован. Оставшиеся клики: ${clicksRemaining}`);

    // Переключаем активную кнопку
    activeButton = activeButton === 'left' ? 'right' : 'left';
    activateButton(activeButton);

    // Проверяем, достиг ли счетчик нуля
    if (clicksRemaining <= 0) {
        clearInterval(timerInterval);
        leftButton.classList.add('inactive');
        rightButton.classList.add('inactive');
    }
});

// Обработка получения флага
socket.on('flag', (data) => {
    showFlag(data.flag);
    // Перезапуск игры через 2 секунды
    setTimeout(initGame, 2000);
});

async function initGame() {
    try {
        // Получаем начальные данные от сервера
        const response = await fetch('/api/init');
        if (!response.ok) {
            throw new Error('Ошибка при инициализации игры');
        }
        const data = await response.json();
        clicksRemaining = data.clicksRemaining;
        sessionId = data.sessionId;
        console.log('Инициализация игры:', data); // Логирование
        clicksDisplay.textContent = clicksRemaining;

        // Сброс таймера
        countdown = 60;
        if (timerDisplay) {
            timerDisplay.textContent = countdown;
        } else {
            console.error('timerDisplay не найден!');
        }

        // Очистка сообщений
        clearMessages();

        // Активируем кнопки
        activeButton = 'left';
        activateButton(activeButton);

        // Регистрация сессии на WebSocket сервере
        socket.emit('register', sessionId);

        // Запуск таймера
        clearInterval(timerInterval);
        timerInterval = setInterval(updateTimer, 1000);
    } catch (error) {
        console.error(error);
        displayError('Не удалось инициализировать игру. Попробуйте перезагрузить страницу.');
    }
}

function updateTimer() {
    countdown--;
    if (timerDisplay) {
        timerDisplay.textContent = countdown;
    } else {
        console.error('timerDisplay не найден при обновлении таймера!');
    }

    if (countdown <= 0) {
        clearInterval(timerInterval);
        showRestartMessage();
        // Перезапуск игры через 2 секунды
        setTimeout(initGame, 2000);
    }
}

function activateButton(button) {
    console.log('Активная кнопка:', button); // Логирование
    if (button === 'left') {
        leftButton.classList.add('active');
        leftButton.classList.remove('inactive');
        rightButton.classList.add('inactive');
        rightButton.classList.remove('active');
    } else {
        rightButton.classList.add('active');
        rightButton.classList.remove('inactive');
        leftButton.classList.add('inactive');
        leftButton.classList.remove('active');
    }
}

async function handleClick(button) {
    if (button !== activeButton) return;

    // Отправляем событие клика через WebSocket
    socket.emit('click');
}

function showFlag(flag) {
    const flagMessage = document.createElement('div');
    flagMessage.classList.add('flag-message');
    flagMessage.textContent = `Флаг: ${flag}`;
    container.appendChild(flagMessage);

    // Автоматически удалять сообщение через 10 секунд
    setTimeout(() => {
        flagMessage.remove();
    }, 10000);
}

function showRestartMessage() {
    // Заменяем содержимое секции таймера на сообщение о перезапуске
    bottomArea.textContent = 'Перезапуск игры...';
}

function clearMessages() {
    const messages = document.querySelectorAll('.flag-message, .error-message, .restart-message');
    messages.forEach(msg => msg.remove());

    // Восстанавливаем содержимое секции таймера
    bottomArea.innerHTML = `Оставшееся время: <span id="timer"></span> секунд`;
    timerDisplay = document.getElementById('timer'); // Обновляем ссылку на timerDisplay
    if (timerDisplay) {
        timerDisplay.textContent = countdown;
    } else {
        console.error('timerDisplay не найден при восстановлении!');
    }
}

leftButton.addEventListener('click', () => handleClick('left'));
rightButton.addEventListener('click', () => handleClick('right'));

window.onload = initGame;
