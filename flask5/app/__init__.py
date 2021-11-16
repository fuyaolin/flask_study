from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask5 import config
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object(config)
db = SQLAlchemy(app)


def create_app():
    # 初始化app配置
    app.secret_key = 'asdfghjkl'
    # 导入数据库和蓝图
    from flask5.app import models, view

    return app
