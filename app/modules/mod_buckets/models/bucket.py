from app import db


class Bucket(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    name = db.Column(db.String(64))
    info = db.Column(db.String(120))
    label = db.Column(db.String(120))
    links = db.relationship('Link', backref='bucket', lazy='dynamic')

    def __repr__(self):
        return f'<Bucket {self.name} created by user: {self.user_id}>'
