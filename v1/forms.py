import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from database import User, session  # Import the User model and session

# class SignUpForm(FlaskForm):
#     first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
#     last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     phone_number = StringField('Phone Number', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
#     submit = SubmitField('Register')


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()]) # Length(min=2, max=50)
    # confirm_email = StringField('Confirm Email', validators=[DataRequired(), Email(), EqualTo('email', message="Emails must match.")])
    phone_number = StringField('Phone Number', validators=[DataRequired()]) # Length(min=2, max=50)
    password = PasswordField('Enter A Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords do not match. Try again!')])


    # Custom validator to check if the email already exists
    def validate_email(self, field):
        email = field.data
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            raise ValidationError('This email is already registered. Please choose a different one.')

    # Custom validator for phone number
    def validate_phone_number(self, field):
        phone_regex = r'^\+\d{1,3}\d{4,14}$'
        if not re.match(phone_regex, field.data):
            raise ValidationError('Phone number must be in international format, e.g., +234XXXXXXXXXX.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
