from flask import Flask
from flask import Response
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
    targets = [key for key in gdata.category if key in request.form]
    return render_template('yin.html', account=account)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/export/xlsx/<account>')
def export_xlsx(account):
    print('export xlsx for account', account)
    # See also: https://github.com/djdmorrison/flask-progress-example
    def export():
        import time
        x = 0
        while x <= 100:
            yield 'data: {}\n\n'.format(x)
            x += 1
            time.sleep(0.1)
    return Response(export(), mimetype='text/event-stream')