from werkzeug.security import generate_password_hash

from mainapp.blog.app import create_app, db


app = create_app()


@app.cli.command('init-db')
def init_db():
    db.create_all()


@app.cli.command('create-users')
def create_users():
    from mainapp.blog.models import User
    db.session.add(
        User(email='ashot@mail.com', password=generate_password_hash('test1'))
    )
    db.session.commit()
