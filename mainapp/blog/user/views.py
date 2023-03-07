from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/')
def user_list():
    from mainapp.blog.models import User
    users = User.query.all()
    return render_template(
        'users/list.html',
        users=users,
    )


@user.route('/<int:pk>')
def get_user(pk: int):
    from mainapp.blog.models import User
    _user = User.query.filter_by(id=pk).one_or_none()
    return render_template(
        'users/details.html',
        user=_user,
    )
