from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    from mainapp.blog.models import User
    users = User.query.all()
    return render_template(
        'users/login.html',
        users=users,
    )


@user.route('/<int:pk>')
def profile(pk: int):
    from mainapp.blog.models import User
    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f"User #{pk} doesn't exist!")
    return render_template(
        'users/profile.html',
        user=_user,
    )
