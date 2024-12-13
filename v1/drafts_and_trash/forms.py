import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from database import User, session  # Import the User model

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone_number = StringField('Phone Number', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    # Custom validator to check if the email already exists
    def validate_email(form, field): # (self, email)
        email = field.data
        existing_user = session.query(User).filter_by(email=email).first() # User.query.filter_by(email=email.data).first()
        if existing_user:
            raise ValidationError('This email is already registered. Please choose a different one.')

    # Custom validator for phone number
    def validate_phone_number(self, phone_number):
        phone_regex = r'^\+\d{1,3}\d{4,14}$'
        if not re.match(phone_regex, phone_number.data):
            raise ValidationError('Phone number must be in international format, e.g., +234XXXXXXXXXX.')

# To encrypt phone numbers (Optional)
from cryptography.fernet import Fernet

# Generate a key (You should save this key securely)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt a phone number
def encrypt_phone(phone_number):
    return cipher_suite.encrypt(phone_number.encode()).decode()

# Decrypt a phone number
def decrypt_phone(encrypted_phone_number):
    return cipher_suite.decrypt(encrypted_phone_number.encode()).decode()

# Example usage (Save encrypted phone number in the database)
# encrypted_phone = encrypt_phone("+234123456789")
# decrypted_phone = decrypt_phone(encrypted_phone)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
