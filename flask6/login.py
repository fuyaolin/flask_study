from flask import Flask
from flask6.sqlhelper import db

app = Flask(__name__)


@app.route('/index')
def index():
    # 返回查询值
    result = db.fetchall("sql")
    return result


if __name__ == '__main__':
    app.run()
