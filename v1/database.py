from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# Load environment variables from .env file
load_dotenv()

# Initialize SQLAlchemy base
Base = declarative_base()

# Phone number encryption
key = Fernet.generate_key()
# print("Encryption key is: {}".format(key))
encryption_key = key
cipher = Fernet(encryption_key)

class User(Base):
    __tablename__ = 'users'
    userId = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    # Encrypted phone number
    phone_number = Column(String(255), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)


# Database connection string from environment variable
db_url = os.getenv('DB_URL')

if not db_url:
    raise ValueError("Database URL not found in environment variables.")

# Create the database engine
engine = create_engine(db_url, echo=True)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()


def create_tables():
    """
    Create tables in the database.
    """
    Base.metadata.create_all(engine)
    print("Tables created successfully.")


def add_user(first_name, last_name, phone_number, email, password):
    """
    Add a new user to the database.
    """
    new_user = User(firstname=first_name, lastname=last_name,
                    phone_number=phone_number, email=email, password=password)
    session.add(new_user)
    session.commit()
    print(f"User {email} added successfully.")


def find_user_by_email(email):
    """
    Find a user by email.
    """
    user = session.query(User).filter_by(email=email).first()
    if user:
        print(f"User found: {user.firstname} {user.lastname}")
    else:
        print("User not found.")
    return user

def encrypt_data(data):
    """
    Encrypt a phone number using Fernet symmetric encryption.
    """
    return cipher.encrypt(data.encode()).decode()


def decrypt_data(encrypted_data):
    """
    Decrypt sensitive data encrypted with Fernet.
    """
    return cipher.decrypt(encrypted_data.encode()).decode()

if __name__ == '__main__':
    # Create tables
    create_tables()

    # Example usage (uncomment to test):
    # add_user("John", "Doe", "+123456789", "john.doe@example.com", "securepassword")
    # find_user_by_email("john.doe@example.com")
