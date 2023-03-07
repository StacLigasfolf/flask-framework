from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "GET":
        return render_template(
            'auth/login.html',
        )

    email = request.form.get('email')
    password = request.form.get('password')

    from mainapp.blog.models import User
    user = User.query().filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Check your login or password')
        return redirect(url_for('.login'))

    return redirect(url_for('users.profile', pk=user.id))


@auth.route('/logout')
def logout():
    return '13'
