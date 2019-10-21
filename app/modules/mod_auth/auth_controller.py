from flask import render_template, flash, redirect, url_for
from flask_login import login_user

from .forms import LoginForm
from .models import User


class AuthController:

    def __init__(self, loginform=LoginForm):
        self.loginForm = loginform()
        self.userModel = User

    def validate_submission(self):
        if self.loginForm.validate_on_submit():
            self.__ceck_user_exist()
        else:
            return render_template('auth/login.html', title='Sign In', form=self.loginForm)


    def __ceck_user_exist(self):
        user = User.query.filter_by(username=self.loginForm.username.data).first()
        if user is None or not user.check_password(self.loginForm.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            login_user(user, remember=self.loginForm.remember_me.data)
            return redirect(url_for('index'))
