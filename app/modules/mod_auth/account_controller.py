from flask import render_template
from flask_login import current_user

from .models import User


class AccountController:

    def render(self):
        user = self.__return_user()
        # TODO: add field in the usermodel to get them dynamic
        bucket_number = 7
        link_number = 30
        return render_template('auth/account.html', user=user, bucket_number=bucket_number, link_number=link_number)

    def __return_user(self):
        user_id = current_user.id
        user = User.query.filter_by(id=user_id).first_or_404()
        return user

