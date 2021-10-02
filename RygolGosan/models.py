from datetime import datetime
from RygolGosan import db, login_manager, bcrypt
from flask_login import UserMixin

# Decorated Function for Login Manager
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

# Sets up the User class for the database with parameters
class User(db.Model, UserMixin):
	# Determines name of said table for database purposes
	#__tablename__ = 'user'

	# Determines properties or columns of said table when the table is created in the database
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique=True, nullable = False)
	email = db.Column(db.String(120), unique=True, nullable = False)
	password = db.Column(db.String(60), nullable=False)
	profile_image_file = db.Column(db.String(20), nullable=False, default='default_image.jpg')
	post = db.relationship('Post', backref='author', lazy=True)
	role = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.password}'"

	@property
	def serialize(self):
		# Return object data in easily serializable format
		return {
			'id': self.id,
			'username': self.username,
			'email': self.email,
			'profile_image': self.profile_image_file,
		}

class Post(db.Model):
	#__tablename__ = 'post'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}'"

	@property
	def serialize(self):
		return {
			'id': self.id,
			'title': self.title,
			'date_posted': self.date_posted,
		}