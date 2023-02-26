from flask import Flask
from mainapp.blog.user.views import user
from mainapp.blog.report.views import report


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
