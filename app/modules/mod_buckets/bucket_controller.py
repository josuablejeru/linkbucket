from flask import render_template, flash, redirect, url_for
from flask_login import current_user
from app import db

from .models import Bucket
from .forms import BucketForm


class BucketController:

    def __init__(self, bucket_id):
        self.bucket_id = bucket_id


    def render(self):
        return render_template('buckets/bucket.html')
