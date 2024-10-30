# !/usr/bin/python3

"""
A Python script that connects to the remote MySQL Database
on the remote server, and creates a table called users there.
The script uses SQLAlchemy to do so.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()  # An instance of the declarative_base class


class User(Base):
    """
    A class that creates a User table in the remote database

    Attributes:
        userId: The user's unique ID
        firstname: User's first name
        lastname: User's last name
        email: User's email address
        password: User's password
    """
    __tablename__ = 'users'  # The table name in the remote database
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    userId = Column(Integer, primary_key=True, autoincrement=True)


# Database Access Variables
remote_user = "dohoudaniel"
password = "dohoudanielfavour200618"
remote_host = "54.236.26.199"
remote_db = "learnopolia"

learnopoliaDBUrl = "mysql://{}:{}@{}/{}".format(
    remote_user, password, remote_host, remote_db)

engine = create_engine(learnopoliaDBUrl, echo=True)
Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# new_user = User(firstname="Daniel", lastname="Dohou", email="dohoudanielfavour@gmail.com", password="dohoudanielfavour16")
# session.add(test_user)
# session.commit()
# session.close()
# print("Connection Succeeded!")
