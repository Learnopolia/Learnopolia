"""
Learnopolia's Flask App
!/usr/bin/python3
"""
from cryptography.fernet import Fernet
from flask import Flask, render_template, redirect, url_for, flash, request, session
from forms import SignUpForm, LoginForm
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from database import add_user, find_user_by_email, decrypt_data, encrypt_data, User
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
from os import getenv


# Load environmental variables from my .env file
load_dotenv()

# app = Flask(__name__)
db = SQLAlchemy()
app = Flask(__name__, static_url_path='/static')
login_manager = LoginManager()
login_manager.init_app(app)
# Redirect to login page if user is not logged in
login_manager.login_view = "loginPage"

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URL')
# app.secret_key = getenv('SECRET_KEY')
app.config['SECRET_KEY'] = 'yoursecretkey'
myDbURL = app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)
db.init_app(app)


# class Users(db.Model):
#     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     firstname = db.Column(db.String(50), nullable=False)
#     lastname = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(100), nullable=False, unique=True)
#     password = db.Column(db.String(100), nullable=False)

@app.route('/')
def loadIndex():
    """
    This function renders the login page when the user requests the home page
    """
    return render_template('/index.html')

@app.route('/about')
def loadAbout():
    """
    This function renders the login page when the user requests an about page
    """
    return render_template('/about.html')


@app.route('/contact')
def loadContact():
    """
    This function renders the login page when the user requests a contact page
    """
    return render_template('/contact.html')


@app.route('/courses')
def loadCourses():
    """
    This function renders the login page when the user requests a courses page
    """
    return render_template('/courses.html')

@app.route('/dashboard')
@login_required
def loadDashboard():
    """
    This function renders the dashboard page when the user is logged in.
    """
    return render_template('dashboard.html')
    # if 'userId' in session:  # Check if the user is logged in
    #     userId = session.get('userId')  # Safely fetch userId from session
    #     try:
    #         user = User.query.get(userId)  # Query the user using the userId
    #         if user:
    #             flash('Login successful! Welcome to your dashboard!', 'success')
    #             return render_template('dashboard.html', user=user)
    #         else:
    #             flash('User not found. Please log in again.', 'error')
    #     except Exception as e:
    #         flash(f"An error occurred: {str(e)}", 'error')
    # else:
    #     flash('You must be logged in to access the dashboard.', 'error')
    # return redirect('/login')
# Redirect to login if not logged in or user not found
# @app.route('/dashboard')
# def loadDashboard():
#     """
#     This function renders the login page when the user requests a login page
#     """
#     if 'userId' in session:
#         userId = session['userId']
#         user = User.query.get(userId)
#         flash('Login successful! Welcome to your dashboard!')
#         return render_template('/dashboard.html', user=user)
#     else:
#         flash('You must be logged in to access the dashboard.')
#         return redirect('/login')
# """
# @app.route('/dashboard')
# def dashboard():
#     # This page is rendered after the user requests a dashboard endpoint
#     # Check if the user is logged in
#     if 'userId' in session:
#         # Retrieve the user's ID from the session
#         userId = session['userId']
#         # Query the database to get the user's information
#         user = Users.query.get(userId)
#         # Render the dashboard template with the user's information
#         return render_template('/dashboard.html', user=user)
#     else:
#         # Redirect to the login page if the user is not logged in
#         return redirect('/login')
# """


# @app.route('/login', methods=['GET', 'POST'])  # Add POST method for login
# def loginPage():
#     form = LoginForm()  # Assuming you create a LoginForm in forms.py
#     if form.validate_on_submit():
#         user = find_user_by_email(form.email.data)  # Check user in database
#         if user and check_password_hash(user.password, form.password.data):
#             session['user_id'] = user.userId  # Store user ID in session
#             flash('Login successful!', 'success')
#             # Redirect to dashboard if successful
#             return redirect('/dashboard')
#         else:
#             flash('Invalid email or password. Please try again.', 'error')
#             # flash('You need to sign up to access the dashboard!', 'error')
#             return redirect('/login')  # Redirect back to login if failed
#     return render_template('login.html', form=form)
@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()  # Assuming LoginForm is correctly defined in forms.py
    if form.validate_on_submit():
        # Ensure the email query works
        user = find_user_by_email(form.email.data)
        if not user:
            flash('Email not found. Please try again or sign up.', 'error')
            return redirect('/login')

        # Check the password hash
        if not check_password_hash(user.password, form.password.data):
            flash('Invalid password. Please try again.', 'error')
            return redirect('/login')

        # Store user in session
        session['userId'] = user.userId  # Ensure consistent key name
        flash('Login successful! Welcome to your dashboard!', 'success')
        return redirect('/dashboard')

    # Handle GET request or failed validation
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field}: {error}", 'error')
    return render_template('login.html', form=form)

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     """
#     This logs the user into the website
#     by checking if the user's email or password
#     corresponds with the one in the backend
#     """
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         # Query the database for a user with the entered email and password
#         user = Users.query.filter_by(email=email, password=password).first()
#         # print(user)
#         if user: # and check_password_hash(user.password, password):
#             # Store the user's ID in the session
#             session['userId'] = user.userId
#             # Redirect to the dashboard or homepage
#             # flash('Login successful! Welcome to your dashboard.')
#             return redirect('/dashboard')
#         else:
#             # Display an error message
#             flash('Invalid email or password.')
#             return render_template('/login.html', error='Invalid email or password')
#     return render_template('/login.html')
# """
# @app.route('/login')
# def loadLogin():
#     This function renders the login page when the user requests a login page
#     return render_template('/login.html')
# """


@app.route('/logout')
def logout():
    """
    Logging out the user
    """
    session.pop('userId', None)
    flash('You have been logged out.')
    return redirect('/login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.confirm_password.errors:
            flash('Invalid email address. Please enter a valid email.', 'error')

        # Hash the password
        hashed_password = generate_password_hash(form.password.data)

        # Encrypt the phone number and email
        # encrypted_email = encrypt_data(form.email.data)
        # encrypted_phone = encrypt_data(form.phone_number.data)

        # Add user to the database
        add_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            # email=encrypted_email,
            # phone_number=encrypted_phone,
            email=form.email.data,
            phone_number=form.phone_number.data,
            password=hashed_password
        )
        # Flash a success message and redirect to the login page
        flash('You have successfully signed up!', 'success')
        return redirect('/login')

    else:
        # Flash all validation errors
        for field, errors in form.errors.items():
            for error in errors:
                flash(error, 'error')
        # Handle form errors
        # if form.confirm_email.errors:
        #     flash('Emails do not match. Please confirm your email correctly.', 'error')



    # Render the signup form with errors (if any)
    return render_template('signup.html', form=form)
# """
# @app.route('/submit')
# def loadSignup():
#     This function renders the login page when the user requests a login page
#     pass
#     # return render_template('/signup.html')
# """
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     """
#     Submitting the user's requests
#     to sign-up or login
#     """
#     if request.method == "POST":
#         firstname = request.form['firstname']
#         lastname = request.form['lastname']
#         email = request.form['email']
#         password = request.form['password']
#         # hashed_password = generate_password_hash(password)
#         new_user = Users(firstname=firstname, lastname=lastname, email=email, password=password)
#         try:
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Registration successful! Please log in.')
#             return redirect('/login')
#         except IntegrityError:
#             db.session.rollback()
#             flash('Email already registered. Please use a different email or log in.')
#             return render_template('/signup.html')
#     return render_template('/signup.html')

# Custom handler for 404 error, and broken pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
