from flask import Flask
from flask import render_template
from flask import request

import gdata

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', category=gdata.category)


@app.route('/yin', methods=['POST'])
def yin():
    account = request.form['account']
    return render_template('yin.html', account=account)


@app.route('/about')
def about():
    return render_template('about.html')
