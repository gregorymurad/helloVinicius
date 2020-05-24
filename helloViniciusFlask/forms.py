from flask_wtf import FlaskForm
from wtforms import StringField

class LoginForm(FlaskForm):
    name = StringField('Name')