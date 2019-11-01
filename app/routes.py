from flask import render_template, redirect, url_for
from flask_login import logout_user, login_required

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
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    return auth_controller.register_user()


@app.route('/user/<user_id>')
@login_required
def account(user_id):
    user_account = AccountController(user_id=user_id)
    return user_account.render()


@app.route('/buckets/<user_id>')
@login_required
def buckets(user_id):
    bucket_controller = BucketController(user_id)
    return bucket_controller.render()
