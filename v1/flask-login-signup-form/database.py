from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

def add_user(first_name, last_name, email, password):
    # Add a new user to the database
    new_user = User(firstname=first_name, lastname=last_name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

def create_tables():
    db.create_all()


def find_user_by_email(email):
    return User.query.filter_by(email=email).first()
