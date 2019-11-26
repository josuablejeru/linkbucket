from flask import render_template


class BucketController:
    """ present and renders a specific bucket """

    def __init__(self, bucket_id):
        self.bucket_id = bucket_id


    def render(self):
        return render_template('buckets/bucket.html')
