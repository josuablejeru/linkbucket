from flask import render_template
from flask_login import current_user

from .models import Bucket
from .forms import BucketForm


class BucketController:

    def __init__(self):
        self.form = BucketForm()

    def render(self):
        buckets = self.__load_buckets()
        return render_template('buckets/list.html', buckets=buckets, bucket_form=self.form)

    def __load_buckets(self):
        user_id = current_user.id
        buckets = Bucket.query.filter_by(user_id=user_id)
        return buckets
