pip3 install flask-bycrypt

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

# Step 2: Import SQLAlchemy
# No need to import Flask or Flask-SQLAlchemy

# Step 3: Configure the database
DB_URL = 'mysql://username:password@localhost/db_name'  # Change this to your database URL
engine = create_engine(DB_URL)

# Step 4: Define the User model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

# Step 5: Create database session
Session = sessionmaker(bind=engine)
session = Session()

# Step 6: Define signup and login functions

def signup(username, email, password):
    # Hash the password before storing it
    hashed_password = generate_password_hash(password)

    # Create a new User object
    new_user = User(username=username, email=email, password=hashed_password)

    # Add the new user to the session
    session.add(new_user)

    try:
        # Commit the session to save changes to the database
        session.commit()
        return True, "User registered successfully"
    except IntegrityError:
        # Handle integrity errors (e.g., duplicate username or email)
        session.rollback()
        return False, "Username or email already exists"

def login(username, password):
    # Query the database for the user with the given username
    user = session.query(User).filter_by(username=username).first()

    # If user exists and password matches, return True
    if user and check_password_hash(user.password, password):
        return True, "Login successful"
    else:
        return False, "Invalid username or password"

# Now you can proceed to use these signup and login functions in your application logic.
# For example, you might call these functions in response to HTTP requests from your frontend.

# Don't forget to close the session when you're done!
session.close()
