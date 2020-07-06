from flask import abort
from flask import Blueprint
from flask import render_template
from jinja2 import TemplateNotFound

from flask import redirect
from flask import url_for
from flask import request

from werkzeug.security import (generate_password_hash,
                                check_password_hash)

from bokio.model.model import User, db

#from bokio.login.login import app

from flask_login import login_user, login_required, logout_user


router = Blueprint('auth', __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/auth/static')


@router.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        user = User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('profile_route.index'))
    else:
        try:
            return render_template('login2.html')
        except TemplateNotFound:
            abort(404)


@router.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            return redirect(url_for('auth.signup'))

        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))
    else:
        try:
            return render_template('signup.html')
        except TemplateNotFound:
            abort(404)


@router.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index_route.index'))
