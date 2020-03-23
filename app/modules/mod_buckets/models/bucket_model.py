from app import db
from sqlalchemy.sql import func


class Bucket(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    name = db.Column(db.String(64))
    info = db.Column(db.String(120))
    label = db.Column(db.String(120))
    links = db.relationship('Link', backref='bucket', lazy='dynamic')
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def get_labels(self):
        return self.label.split(';')

    def set_label(self, label):
        self.label = self.label + ';' + str(label)

    def __repr__(self):
        return f'<Bucket {self.name} created by user: {self.user_id}>'
