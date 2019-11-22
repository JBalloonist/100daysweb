from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class StoreForm(FlaskForm):
    storeid = StringField('Store ID', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    gallons = IntegerField('Gallons', validators=[DataRequired(message='Value must be a number')])
    cost = IntegerField('Cost', validators=[DataRequired('Value must be a number')])
    submit = SubmitField('Submit')
