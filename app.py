from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def home():
    try:
        # Запрашиваем случайную цитату с zenquotes.io
        response = requests.get('https://zenquotes.io/api/random')

        if response.status_code == 200:
            data = response.json()
            quote = data[0]['q']  # текст цитаты
            author = data[0]['a']  # автор
        else:
            quote = "Не удалось получить цитату. Попробуйте обновить страницу."
            author = "Система"

    except Exception as e:
        quote = f"Ошибка при получении цитаты: {str(e)}"
        author = "Система"

    return render_template('index.html', quote=quote, author=author)


@app.route('/refresh')
def refresh():
    # Перезагружаем страницу с новой цитатой
    return home()


if __name__ == '__main__':
    app.run(debug=True)