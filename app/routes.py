from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

import sys

@app.route('/')
@app.route('/index')
def hello():
    user = {
        'username': 'Josua'
    }
    return render_template('index.html', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)
