from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        state = request.form['state']
        category = request.form['category']
        response = requests.get('https://api-recomendaciones.onrender.com')
        data = response.json()
        return render_template('results.html', results=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
