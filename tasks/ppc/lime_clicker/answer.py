import requests
import time

session = requests.Session()

# Инициализация игры
init_response = session.get('http://localhost:3000/api/init').json()
session_id = init_response['sessionId']
clicks_remaining = init_response['clicksRemaining']

print(f"Начинаем игру. Осталось кликов: {clicks_remaining}")

# Время начала
start_time = time.time()

while clicks_remaining > 0:
    # Отправляем запрос на клик
    click_response = session.post('http://localhost:3000/api/click', json={'sessionId': session_id}).json()
    
    if not click_response['success']:
        print(f"Ошибка: {click_response['message']}")
        break

    clicks_remaining = click_response.get('clicksRemaining', 0)
    flag = click_response.get('flag')

    if flag:
        print(f"Получен флаг: {flag}")
        break

    print(f"Осталось кликов: {clicks_remaining}")

    # Задержка 25 мс
    time.sleep(0.025)

    # Проверка таймера
    if time.time() - start_time > 30:
        print("Время истекло")
        break
