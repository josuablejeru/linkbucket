from datetime import datetime

from app import db


class Link(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(20), index=True)
    bucket_id = db.Column(db.Integer(), db.ForeignKey('bucket.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    url = db.Column(db.String(512))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f'<Link {self.title}; bucket:{self.bucket_id}; user: {self.user_id}>'
