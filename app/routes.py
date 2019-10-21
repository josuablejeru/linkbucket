from flask import render_template, redirect, url_for
from flask_login import logout_user, login_required

from app import app
from app.modules.mod_auth.auth_controller import AuthController


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    auth_controller = AuthController()
    return auth_controller.validate_submission()



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
