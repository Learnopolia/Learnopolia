"""
Learnopolia's Flask App

!/usr/bin/python3
"""

from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from dotenv import load_dotenv
import os


# Load environmental variables from my .env filw
load_dotenv()

# app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.secret_key = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)


class Users(db.Model):
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)


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
def loadDashboard():
    """
    This function renders the login page when the user requests a login page
    """
    if 'userId' in session:
        userId = session['userId']
        user = Users.query.get(userId)
        flash('Login successful! Welcome to your dashboard!')
        return render_template('/dashboard.html', user=user)
    else:
        flash('You must be logged in to access the dashboard.')
        return redirect('/login')
"""
@app.route('/dashboard')
def dashboard():
    # This page is rendered after the user requests a dashboard endpoint
    # Check if the user is logged in
    if 'userId' in session:
        # Retrieve the user's ID from the session
        userId = session['userId']
        # Query the database to get the user's information
        user = Users.query.get(userId)
        # Render the dashboard template with the user's information
        return render_template('/dashboard.html', user=user)
    else:
        # Redirect to the login page if the user is not logged in
        return redirect('/login')
"""


@app.route('/')
def loadIndex():
    """
    This function renders the login page when the user requests the home page
    """
    return render_template('/index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This logs the user into the website
    by checking if the user's email or password
    corresponds with the one in the backend
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Query the database for a user with the entered email and password
        user = Users.query.filter_by(email=email, password=password).first()
        # print(user)
        if user: # and check_password_hash(user.password, password):
            # Store the user's ID in the session
            session['userId'] = user.userId
            # Redirect to the dashboard or homepage
            # flash('Login successful! Welcome to your dashboard.')
            return redirect('/dashboard')
        else:
            # Display an error message
            flash('Invalid email or password.')
            return render_template('/login.html', error='Invalid email or password')
    return render_template('/login.html')
"""
@app.route('/login')
def loadLogin():
    This function renders the login page when the user requests a login page
    return render_template('/login.html')
"""


@app.route('/logout')
def logout():
    """
    Logging out the user
    """
    session.pop('userId', None)
    flash('You have been logged out.')
    return redirect('/login')


"""
@app.route('/submit')
def loadSignup():
    This function renders the login page when the user requests a login page
    pass
    # return render_template('/signup.html')
"""

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Submitting the user's requests
    to sign-up or login
    """
    if request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        # hashed_password = generate_password_hash(password)
        new_user = Users(firstname=firstname, lastname=lastname, email=email, password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.')
            return redirect('/login')
        except IntegrityError:
            db.session.rollback()
            flash('Email already registered. Please use a different email or log in.')
            return render_template('/signup.html')
    return render_template('/signup.html')



if __name__ == '__main__':
    app.secret_key = 'your_secret_key'
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=5000) #, debug=True)
