from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app import db

from .models import Bucket
from .forms import BucketForm


class BucketController:

    def __init__(self):
        self.form = BucketForm()
        self.model = Bucket

    def render(self):
        buckets = self.__load_buckets()
        return render_template('buckets/list.html', buckets=buckets, bucket_form=self.form)

    def __load_buckets(self):
        user_id = current_user.id
        buckets = self.model.query.filter_by(user_id=user_id)
        return buckets

    def create_bucket(self):
        if self.form.validate_on_submit() is True:
            self.__commit_bucket(self.form, self.model)
            return redirect(url_for('buckets'))
        else:
            return redirect(url_for('buckets'))

    def __commit_bucket(self, form, model):
        # TODO: implement seter and geter for labels
        bucket = model(user_id=current_user.id, name=form.name.data, info=form.info.data, label='')
        db.session.add(bucket)
        db.session.commit()
        flash('Bucket Created')
