from app import db


class Bucket(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))
    name = db.Column(db.String(64))
    info = db.Column(db.String(120))
    label = db.Column(db.String(120))
    links = db.relationship('Link', backref='bucket', lazy='dynamic')

    def get_labels(self):
        return self.label.split(';')

    def set_label(self, label):
        self.label = self.label + ';' + str(label)

    def __repr__(self):
        return f'<Bucket {self.name} created by user: {self.user_id}>'
