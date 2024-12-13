# # # from sqlalchemy import create_engine
# # from sqlalchemy.ext.declarative import declarative_base
# # # from sqlalchemy.orm import sessionmaker
# # # Assuming your User model and db instance are in 'database.py'
# # from database import db
# # from flask import Flask
# # import os

# # # Define a function to connect to the database

# # db_url = os.getenv('SQLALCHEMY_DATABASE_URI')

# # def create_user_table():
# #     # Create a Flask app instance
# #     app = Flask(__name__)

# #     # Set the SQLALCHEMY_DATABASE_URI
# #     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# #     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# #     # Initialize the database with the app context
# #     db.init_app(app)

# #     # Create the User table within the app context
# #     with app.app_context():
# #         db.create_all()
# #         print("User table created successfully.")
# #     # # Get the database URL
# #     # database_url = get_database_url()

# #     # # Create the engine using the database URL
# #     # engine = create_engine(database_url)

# #     # # Bind the engine to the database metadata
# #     # db.metadata.bind = engine

# #     # # Create the User table in the database
# #     # # db.create_all()
# #     # print("User table created successfully.")


# # if __name__ == '__main__':
# #     create_user_table()


# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env
# load_dotenv()

# # Initialize the SQLAlchemy object
# db = SQLAlchemy()

# def create_user_table():
#     # Create a Flask app instance
#     app = Flask(__name__)

#     # Get the database URL from environment or fallback
#     db_url = os.getenv('SQLALCHEMY_DATABASE_URI')

#     # Set the SQLALCHEMY_DATABASE_URI
#     app.config['SQLALCHEMY_DATABASE_URI'] = db_url
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Initialize the database with the app context
#     db.init_app(app)

#     # Create the User table within the app context
#     with app.app_context():
#         db.create_all()
#         print("User table created successfully.")

# if __name__ == '__main__':
#     create_user_table()
