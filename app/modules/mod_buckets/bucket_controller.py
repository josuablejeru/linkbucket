from flask import render_template

from .models import Bucket


class BucketController:

    def __init__(self, user):
        self.user = user

    def render(self):
        buckets = self.__load_buckets()
        return render_template('buckets/list.html', buckets=buckets)


    def __load_buckets(self):
        buckets = Bucket.query.filter_by(user.id)
        return buckets
