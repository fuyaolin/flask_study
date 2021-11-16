from flask import Flask
from flask7 import config

app = Flask(__name__)
app.config.from_object(config.setting)


@app.route('/index')
def index():
    return "result"


if __name__ == '__main__':
    app.run()
