from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    import json
    with open('appdata/category.json', 'r') as f:
        category = json.load(f)
    return render_template('index.html', category=category)


@app.route('/yin', methods=['POST'])
def yin():
    account = request.form['account']
    return render_template('yin.html', account=account)


@app.route('/about')
def about():
    return render_template('about.html')
