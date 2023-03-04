from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from mainapp.blog.report.views import report
from mainapp.blog.user.views import user

db = SQLAlchemy()


def create_app() -> Flask:
    app = Flask(__name__)
    # app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = 'cb02820a3e94d72c9f950ee10ef7e3f7a35b3f5b'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    db.init_app(app)

    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)



