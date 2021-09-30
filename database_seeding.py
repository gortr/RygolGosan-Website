from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api import Base, User

engine = create_engine('sqlite:///sitedatabase.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Create dummy user
user_1 = User(
    username="Rygol", 
    email="rygol@protonmail.com", 
    picture="https://cdn2.iconfinder.com/data/icons/happy-users/100/users09-512.png",
    password="ChangeMePlease",
    role="Administrator")

session.add(user_1)
session.commit()