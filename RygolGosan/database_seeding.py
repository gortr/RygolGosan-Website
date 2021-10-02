from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///site.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user_1 = User(
    username = "Rygol", 
    email = "rygol@protonmail.com", 
    picture = "https://cdn2.iconfinder.com/data/icons/happy-users/100/users09-512.png",
    hashed_password = bcrypt.generate_password_hash(ChangeMePlease).decode('utf-8'),
    password = hashed_password,
    role = "Administrator")

session.add(user_1)
session.commit()