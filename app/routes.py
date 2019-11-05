from flask import render_template, redirect, url_for
from flask_login import logout_user, login_required, current_user

from app import app
from app.modules.mod_auth import AccountController, AuthController
from app.modules.mod_buckets import BucketController

auth_controller = AuthController()


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return auth_controller.validate_submission()


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    return auth_controller.register_user()


@app.route('/account')
@login_required
def account():
    user_account = AccountController()
    return user_account.render()


@app.route('/buckets')
@login_required
def buckets():
    bucket_controller = BucketController()
    return bucket_controller.render()
