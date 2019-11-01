from flask import render_template, redirect, url_for
from flask_login import logout_user, login_required

from app import app
from app.modules.mod_auth import AccountController, AuthController

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


@app.route('/user/<username>')
@login_required
def account(username):
    user_account = AccountController(username=username)
    return user_account.render()


@app.route('/buckets')
@login_required
def buckets():
    # bucket_controller = BucketController()
    # return bucket_controller.render()
    return 'hallo'
