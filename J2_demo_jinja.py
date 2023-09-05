from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def demo() -> str:
    return 'Coucou l\'ISEP !'

@app.route('/coucou')
def coucou() -> 'html':
    # ATTENTION : "coucou.html" doit être placé dans un dossier "templates/"
    return render_template('coucou.html', date=datetime.now())

app.run(host="0.0.0.0")
