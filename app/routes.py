from flask import render_template, redirect, url_for, request
from flask_login import logout_user, login_required

from app.modules.mod_auth import AccountController, AuthController
from app.modules.mod_buckets import BucketListController, BucketController


def config_routes(app):

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
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        auth_controller = AuthController()
        return auth_controller.register_user()

    @app.route('/account', methods=['GET'])
    @login_required
    def account():
        user_account = AccountController()
        return user_account.render()

    @app.route('/buckets', methods=['GET', 'POST'])
    @login_required
    def buckets():
        bucketlist_controller = BucketListController()

        if request.method == 'GET':
            return bucketlist_controller.render()

        if request.method == 'POST':
            return bucketlist_controller.create_bucket()

    @app.route('/buckets/<int:bucket_id>', methods=['GET'])
    @login_required
    def bucket(bucket_id):
        bucket_controller = BucketController(bucket_id)
        return bucket_controller.render()
