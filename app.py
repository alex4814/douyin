from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/yin', methods=['POST'])
def yin():
    account = request.form['account']
    return render_template('yin.html', account=account)
