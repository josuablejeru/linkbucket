from app import db

from sqlalchemy.sql import func

class Link(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(20), index=True)
    bucket_id = db.Column(db.Integer(), db.ForeignKey('bucket.id'))
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    url = db.Column(db.String(512))
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f'<Link {self.title}; bucket:{self.bucket_id}; user: {self.user_id}>'
