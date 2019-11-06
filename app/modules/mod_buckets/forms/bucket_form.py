from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BucketForm(FlaskForm):
    name = StringField('name', validators=[DataRequired])
    info = StringField('info')
    create = SubmitField('Create Bucket')
