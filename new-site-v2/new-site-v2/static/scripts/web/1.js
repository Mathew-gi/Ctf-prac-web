let clicks = 0;
let lastClickTime = null;
const clickButton = document.getElementById('click-button');
const clickCounter = document.getElementById('click-counter');
const timerMessage = document.getElementById('timer-message');
const flagMessage = document.getElementById('flag-message');
const cooldownTime = 1000; // 1 минута в миллисекундах

function incrementClick() {
    clicks++;
    clickCounter.textContent = `Клики: ${clicks}`;

    if (clicks >= 10) {
        flagMessage.style.display = "block"; // Показать флаг
        return;
    }

    lastClickTime = Date.now();
    clickButton.disabled = true; // Блокируем кнопку
    updateCooldownMessage();
}

function updateCooldownMessage() {
    if (lastClickTime === null) return;

    const timeSinceLastClick = Date.now() - lastClickTime;
    const timeRemaining = cooldownTime - timeSinceLastClick;

    if (timeRemaining <= 0) {
        clickButton.disabled = false;
        timerMessage.textContent = "Нажмите на кнопку, чтобы продолжить.";
        lastClickTime = null; // Сбрасываем откат
    } else {
        timerMessage.textContent = `Ожидайте ${Math.ceil(timeRemaining / 1000)} секунд, прежде чем нажать снова.`;
        setTimeout(updateCooldownMessage, 1000); // Обновляем каждую секунду
    }
}

// Инициализация
clickCounter.textContent = "Клики: 0";
timerMessage.textContent = "Нажмите на кнопку, чтобы начать.";
