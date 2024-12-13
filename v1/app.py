from cryptography.fernet import Fernet
from flask import Flask, render_template, redirect, url_for, flash, request, session
from forms import SignUpForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from database import add_user, find_user_by_email, User
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv

# Load environmental variables from .env file
load_dotenv()

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'yoursecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Logging database queries for email
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Custom function to check if user is logged in
def is_logged_in():
    return 'user_id' in session


@app.route('/')
def loadIndex():
    return render_template('index.html')


@app.route('/about')
def loadAbout():
    return render_template('about.html')


@app.route('/contact')
def loadContact():
    return render_template('contact.html')


@app.route('/courses')
def loadCourses():
    return render_template('courses.html')


@app.route('/dashboard')
def loadDashboard():
    # Check if user is logged in via the session
    if not is_logged_in():
        flash('You need to be logged in to access the dashboard.', 'error')
        return redirect('/login')
    return render_template('dashboard.html')


@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    form = LoginForm()
    if form.validate_on_submit():
        user = find_user_by_email(form.email.data)
        if not user:
            flash('Email not found. Please try again or sign up.', 'error')
            return redirect('/login')

        if not check_password_hash(user.password, form.password.data):
            flash('Invalid password. Please try again.', 'error')
            return redirect('/login')

        session['user_id'] = user.userId
        flash('Login successful! Welcome to your dashboard!', 'success')
        return redirect('/dashboard')

    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field}: {error}", 'error')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect('/login')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.password.data != form.confirm_password.data:
            flash('Passwords do not match. Please try again.', 'error')
            return redirect('/signup')

        hashed_password = generate_password_hash(form.password.data)
        add_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            password=hashed_password
        )
        flash('You have successfully signed up!', 'success')
        return redirect('/login')

    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{field}: {error}", 'error')
    return render_template('signup.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
