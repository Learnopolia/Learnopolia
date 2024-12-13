from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)  # Create a Flask web application instance
# Configure SQLAlchemy to use MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)  # Create a SQLAlchemy database instance

# Define a User class as a SQLAlchemy model to represent the users table in the database


class User(db.Model):
    # Primary key column for user ID
    id = db.Column(db.Integer, primary_key=True)
    # Column for username, unique and not null
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Column for email, unique and not null
    email = db.Column(db.String(100), unique=True, nullable=False)
    # Column for hashed password, not null
    password = db.Column(db.String(100), nullable=False)

# Route for the sign-up page


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':  # If the form is submitted via POST method
        username = request.form['username']  # Get username from the form
        email = request.form['email']  # Get email from the form
        password = request.form['password']  # Get password from the form

        hashed_password = generate_password_hash(
            password)  # Hash the password for security

        new_user = User(username=username, email=email,
                        password=hashed_password)  # Create a new User object

        try:
            # Add the new user to the database session
            db.session.add(new_user)
            db.session.commit()  # Commit the changes to the database
            # Redirect to the login page after successful sign-up
            return redirect(url_for('login'))
        except IntegrityError:
            # Rollback changes if there's an IntegrityError (e.g., duplicate username or email)
            db.session.rollback()
            # Render the signup page with an error message
            return render_template('signup.html', error="Username or email already exists.")

    return render_template('signup.html')  # Render the signup page

# Route for the login page


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # If the form is submitted via POST method
        username = request.form['username']  # Get username from the form
        password = request.form['password']  # Get password from the form

        # Query the database for the user with the given username
        user = User.query.filter_by(username=username).first()

        # If user exists and password matches
        if user and check_password_hash(user.password, password):
            # Redirect to dashboard or home page after successful login
            return redirect(url_for('dashboard'))
        else:
            # Render the login page with an error message for invalid username or password
            return render_template('login.html', error="Invalid username or password.")

    return render_template('login.html')  # Render the login page


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
