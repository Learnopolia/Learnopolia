# # from flask_sqlalchemy import SQLAlchemy
# # db = SQLAlchemy()


# # class User(db.Model):
# #     __tablename__ = 'users'
# #     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     firstname = db.Column(db.String(50), nullable=False)
# #     lastname = db.Column(db.String(50), nullable=False)
# #     # Encrypted phone number
# #     phone_number = db.Column(db.String(255), nullable=False)
# #     email = db.Column(db.String(50), nullable=False, unique=True)
# #     password = db.Column(db.String(255), nullable=False)


# # def add_user(first_name, last_name, email, password):
# #     # Add a new user to the database
# #     new_user = User(firstname=first_name, lastname=last_name,
# #                     email=email, password=password)
# #     db.session.add(new_user)
# #     db.session.commit()


# # def create_tables():
# #     db.create_all()


# # def find_user_by_email(email):
# #     return User.query.filter_by(email=email).first()

# # if __name__ == '__main__':
# #     create_tables()
# #
# #
# #
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import os
# from dotenv import load_dotenv

# load_dotenv()

# # Initialize the SQLAlchemy object
# db = SQLAlchemy()


# # Define the User model
# class User(db.Model):
#     __tablename__ = 'users'
#     userId = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     firstname = db.Column(db.String(50), nullable=False)
#     lastname = db.Column(db.String(50), nullable=False)
#     # Encrypted phone number
#     phone_number = db.Column(db.String(255), nullable=False)
#     email = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)


# def add_user(first_name, last_name, email, password):
#     """
#     Add a new user to the database.
#     """
#     new_user = User(firstname=first_name, lastname=last_name,
#                     email=email, password=password)
#     db.session.add(new_user)
#     db.session.commit()


# def find_user_by_email(email):
#     """
#     Find a user by email.
#     """
#     return User.query.filter_by(email=email).first()


# # def create_tables():
# #     """
# #     Create tables in the database.
# #     """
# #     # Create the Flask app instance


#     # Initialize the database with the app
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#         print("Tables created successfully.")


# if __name__ == '__main__':
#     db = SQLAlchemy()
#     # Initializing the Flask App
#     app = Flask(__name__)
#     # print(os.getenv('DB_URL'))
#     # Set the database URI (use environment variables for security)
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Create tables
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#         print("Tables created successfully.")
