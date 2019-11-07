from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user
from werkzeug.urls import url_parse

from app import db
from .forms import LoginForm, RegistrationForm
from .models import User


class AuthController:

    def __init__(self, login_form=LoginForm, registration_form=RegistrationForm, user_model=User):
        self.login_form = login_form
        self.registration_form = registration_form
        self.user_model = user_model

    def validate_submission(self):

        login_form = self.login_form()

        if login_form.validate_on_submit() is True:
            return self.__check_user_exist()
        else:
            return render_template('auth/login.html', title='Sign In', form=login_form)

    def register_user(self):

        registration_form = self.registration_form()

        if current_user.is_authenticated:
            return redirect(url_for('index'))

        if registration_form.validate_on_submit():
            user = User(username=registration_form.username.data, email=registration_form.email.data)
            user.set_password(registration_form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Success!')
            return redirect(url_for('login'))
        return render_template('auth/regristation.html', title='Register', form=registration_form)

    def __check_user_exist(self):
        """ check if a user exist in the db """

        login_form = self.login_form()

        user = User.query.filter_by(username=login_form.username.data).first()
        if user is None or not user.get_password(login_form.password.data):
            flash('Invalid username or password')  # TODO: flash in Template hinzufuegen
            return redirect(url_for('login'))

        login_user(user, remember=login_form.remember_me.data)

        next_page = request.args.get('next')

        # if 'next' is found and the host is specified
        # it will redirect
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
