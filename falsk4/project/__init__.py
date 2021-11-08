from flask import Flask
from project.views.first import FIRST
from project.views.second import SECOND

def create_app():
    app = Flask(__name__)
    app.secret_key = 'asdfghjkl'

    @app.route('/')
    def index():
        return 'index'

    app.register_blueprint(FIRST)
    app.register_blueprint(SECOND)

    return app