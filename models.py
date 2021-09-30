from __main__ import login_manager
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime
from flask_login import UserMixin

# Declaring Instances and/or Variables
Base = declarative_base()

# Decorated Function for Login Manager
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# Sets up the User class for the database with parameters
class User(Base, UserMixin):
	# Determines name of said table for database purposes
	__tablename__ = 'user'

	# Determines properties or columns of said table when the table is created in the database
	id = Column(Integer, primary_key = True)
	username = Column(String(20), unique=True, nullable = False)
	email = Column(String(120), unique=True, nullable = False)
	profile_image_file = Column(String(20), nullable=False, default='default_image.jpg')
	password = Column(String(60), nullable=False)
	post = relationship('Post', backref='author', lazy=True)
	role = Column(String(20), nullable=False)

	@property
	def serialize(self):
		# Return object data in easily serializable format
		return {
			'id': self.id,
			'username': self.username,
			'email': self.email,
			'profile_image': self.profile_image_file,
		}

class Post(Base):
	__tablename__ = 'post'

	id = Column(Integer, primary_key=True)
	title = Column(String(100), nullable=False)
	date_posted = Column(DateTime, nullable=False, default=datetime.utcnow)
	content = Column(Text, nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'date_posted': self.date_posted,
		}



####### insert at end of file ######

engine = create_engine('sqlite:///site.db', echo=True)
Base.metadata.create_all(engine)