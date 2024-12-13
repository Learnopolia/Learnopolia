from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from database import db, User  # Assuming your User model and db instance are in 'database.py'
import os

# Define a function to connect to the database
def get_database_url():
    """
    Get the custom database URL from an environment variable
    or specify it manually.
    Example format (PostgreSQL):
    'postgresql://username:password@hostname/database_name'
    """
    db_url = 'mysql://{}:{}@{}/{}'.format(os.getenv('USER'), os.getenv('PASSWORD'), os.getenv('HOST'), os.getenv('DATABASE'))
    return db_url

def create_user_table():
    # Get the database URL
    database_url = get_database_url()

    # Create the engine using the database URL
    engine = create_engine(database_url)

    # Bind the engine to the database metadata
    db.metadata.bind = engine

    # Create the User table in the database
    db.create_all()
    print("User table created successfully.")

if __name__ == '__main__':
    create_user_table()
