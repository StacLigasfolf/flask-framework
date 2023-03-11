import click
from werkzeug.security import generate_password_hash

from mainapp.blog.extensions import db


@click.command('create-init-user')
def create_init_user():
    from mainapp.blog.models import User
    from mainapp.wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('test123'))
        )
        db.session.commit()
