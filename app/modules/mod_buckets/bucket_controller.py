from flask import render_template
from flask_login import current_user

from .models import Bucket


class BucketController:

    def render(self):
        buckets = self.__load_buckets()
        return render_template('buckets/list.html', buckets=buckets)

    def __load_buckets(self):
        buckets = Bucket.query.filter_by(user_id=current_user.id)
        return buckets
