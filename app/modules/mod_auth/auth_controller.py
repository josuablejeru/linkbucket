from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user
from werkzeug.urls import url_parse

from .forms import LoginForm
from .models import User


class AuthController:

    def __init__(self, loginform=LoginForm):
        self.login_form = loginform()
        self.userModel = User

    def validate_submission(self):
        if self.login_form.validate_on_submit() is True:
            return self.__ceck_user_exist()
        else:
            return render_template('auth/login.html', title='Sign In', form=self.login_form)


    def __ceck_user_exist(self):
        user = User.query.filter_by(username=self.login_form.username.data).first()
        if user is None or not user.get_password(self.login_form.password.data):
            flash('Invalid username or password')  # TODO: flash in Template hinzufuegen
            return redirect(url_for('login'))

        login_user(user, remember=self.login_form.remember_me.data)

        next_page = request.args.get('next')

        # if 'next' is found and the host is specified
        # it will redirect
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
