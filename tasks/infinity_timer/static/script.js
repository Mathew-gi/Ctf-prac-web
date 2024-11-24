(function() {
    var timerElement = document.getElementById('timer');
    var remainingTime = parseInt(timerElement.textContent);

    // Обновление таймера каждую секунду
    var countdown = setInterval(function() {
        remainingTime--;
        timerElement.textContent = remainingTime;

        if (remainingTime <= 0) {
            clearInterval(countdown);
            alert('Лайм испортился. Попробуйте снова.');
            // Интересно, что мой братский скрипт делает...
            location.reload();
        }
    }, 1000);
})();
