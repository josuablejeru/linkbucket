from app import db


class Bucket(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    name = db.Column(db.String(64), index=True)
    info = db.Column(db.String(120))
    label = db.Column(db.String(120))

    def __repr__(self):
        return f'<Bucket {self.name} created by user: {self.user_id}>'
