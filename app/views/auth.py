import datetime

from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from app.forms import RegisterForm, LoginForm
from app.models.user import User
from app.services.base_auth_service import BaseAuthService

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register', methods=['POST', 'GET'])
def register(auth_service: BaseAuthService):
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(account=form.username.data,
                        password=form.password.data,
                        name=form.name.data,
                        email=form.email.data,
                        type='1',
                        is_notification=1,
                        notification_method=1,
                        create_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        modify_date=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            if auth_service.register(user):
                flash('Thanks for registering', 'success')
                return redirect(url_for('auth.login'))
            else:
                flash('Registering fail', 'danger')

    return render_template('auth/register.html', form=form, current_user=current_user)


@auth.route('/login', methods=['GET', 'POST'])
def login(auth_service: BaseAuthService):
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            remember = form.remember.data
            user = User(account=form.username.data,
                        password=form.password.data)

            if auth_service.is_valid_login(user):
                user = auth_service.get_user_by_account(user)
                login_user(user=user, remember=remember)
                flash('Login success', 'success')
                return redirect(url_for('wish_list.index'))
            else:
                flash('Login fail', 'danger')

    return render_template('auth/login.html', form=form, current_user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Bye Bye', 'success')
    return redirect(url_for('auth.login'))
