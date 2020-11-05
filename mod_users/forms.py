from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
