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


@click.command('create-init-tags')
def create_init_tags():
    from mainapp.blog.models import Tag
    from mainapp.wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
