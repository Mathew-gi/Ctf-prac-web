from flask import Flask, render_template, request, redirect, url_for, session, abort
import time

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на случайный секретный ключ в продакшене

@app.route('/')
def index():
    # Получаем системное время клиента из заголовка 'X-Client-Time'
    client_time = request.headers.get('X-Client-Time')

    if not client_time:
        # Если заголовок отсутствует, отображаем обычный таймер
        return render_template('index.html', remaining_time=60)

    try:
        # Преобразуем client_time в число
        client_time = float(client_time)
    except ValueError:
        client_time = 0

    # Код символа бесконечности
    infinity_code = ord('∞')  # Unicode код символа бесконечности

    if client_time == infinity_code:
        # Устанавливаем сессионную переменную
        session['infinite_time'] = True
        session['start_time'] = time.time()
        # Отображаем страницу с ∞ секунд
        return render_template('waiting.html', remaining_time='∞')
    else:
        # Отображаем обычный таймер
        return render_template('index.html', remaining_time=60)

@app.route('/check_progress')
def check_progress():
    if session.get('infinite_time'):
        # Проверяем, прошло ли 10 секунд
        elapsed_time = time.time() - session.get('start_time', 0)
        if elapsed_time >= 10:
            # Перенаправляем на страницу с флагом
            return redirect(url_for('flag'))
        else:
            # Продолжаем ожидание
            return render_template('waiting.html', remaining_time='∞')
    else:
        # Если сессия не установлена, перенаправляем на главную
        return redirect(url_for('index'))

@app.route('/flag')
def flag():
    if session.get('infinite_time') and (time.time() - session.get('start_time', 0)) >= 10:
        # Очищаем сессию и отображаем флаг
        session.clear()
        flag = 'limeCTF{tim3_1s_r3lativ3}'
        return render_template('flag.html', flag=flag)
    else:
        # Доступ запрещен
        return abort(403)

@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
