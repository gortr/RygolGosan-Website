from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Length, Email, EqualTo, ValidationError
from models import User

# Setup for a Public Account User to Register for the Web Application
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[InputRequired(), DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[InputRequired(), DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is already taken. Please use a different username.')

    def validate_email(self, email):

        email = User.query.filter_by(email=email.data).first()

        if email:
            raise ValidationError('That email is already being used. Please use a different email.')

# Allows for a User to Log In using their Member Account for the Web Application
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), DataRequired(), Length(min=6, max=15)])
    email = StringField('Email',
                        validators=[InputRequired(), DataRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), DataRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')