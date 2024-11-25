import requests
import time

# Настройка
session = requests.Session()
BASE_URL = 'http://90.156.156.157:3000'

# Инициализация
response = session.get(f'{BASE_URL}/api/init').json()
session_id = response['sessionId']
clicks_remaining = response['clicksRemaining']

print(f"Начинаем игру. Осталось кликов: {clicks_remaining}")

# Цикл кликов
while clicks_remaining > 0:
    # Отправляем запрос на клик
    response = session.post(f'{BASE_URL}/api/click', json={'sessionId': session_id}).json()
    
    clicks_remaining = response.get('clicksRemaining', 0)
    flag = response.get('flag')
    
    if flag:
        print(f"Получен флаг: {flag}")
        break

    # Задержка для соблюдения ограничения сервера
    time.sleep(0.01)
    
    print(f"Начинаем игру. Осталось кликов: {clicks_remaining}")
print("Игра завершена.")
