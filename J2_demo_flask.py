from flask import Flask

app = Flask(__name__)


@app.route('/')
def demo() -> str:
    return 'Coucou l\'ISEP !'


app.run(host="0.0.0.0")
