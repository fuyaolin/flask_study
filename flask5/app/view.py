# 蓝图
from flask5.app import app
from flask5.app.views.student import STUDENT

app.register_blueprint(STUDENT)
