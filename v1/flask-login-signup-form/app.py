from flask import Flask, render_template, redirect, url_for, flash, request, session
# Assuming you have a LoginForm in your forms.py
from forms import SignUpForm, LoginForm
# Add this function to your database module
from database import db, create_tables, add_user, find_user_by_email
from werkzeug.security import generate_password_hash, check_password_hash
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yoursecretkey'

USER = getenv('USER')
PASSWORD = getenv('PASSWORD')
HOST = getenv('HOST')
DATABASE = getenv('DATABASE')

if not all([USER, PASSWORD, HOST, DATABASE]):
    raise ValueError("Database environment variables are not set properly.")

myDbURL = f'mysql://{USER}:{PASSWORD}@{HOST}/{DATABASE}'
app.config['SQLALCHEMY_DATABASE_URI'] = myDbURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route('/')  # Displaying the home page
def homePage():
    """
    This function renders the home page when the
    route requested is '/'
    """
    return render_template('/index.html')


@app.route('/login', methods=['GET', 'POST'])  # Add POST method for login
def loginPage():
    form = LoginForm()  # Assuming you create a LoginForm in forms.py
    if form.validate_on_submit():
        user = find_user_by_email(form.email.data)  # Check user in database
        if user and check_password_hash(user.password, form.password.data):
            session['user_id'] = user.userId  # Store user ID in session
            # Redirect to dashboard if successful
            return redirect('/dashboard')
        else:
            flash('You need to sign up to access the dashboard!', 'error')
            return redirect('/login')  # Redirect back to login if failed
    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        add_user(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hashed_password
        )
        flash('You have successfully signed up!', 'success')
        return redirect('/login')
    return render_template('signup.html', form=form)


@app.route('/dashboard')
def dashboardPage():
    # Check if user is logged in
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect('/login')  # Redirect to login if not logged in
    return render_template('dashboard.html')


@app.route('/logout')  # Optional: Add a logout route
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    flash('You have been logged out.', 'success')
    return redirect('/login')


if __name__ == '__main__':
    with app.app_context():
        create_tables()
    app.run(debug=True)
