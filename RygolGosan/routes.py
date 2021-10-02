# Imports Main App & Flask Components for Routing
from flask import render_template, url_for, request, redirect, flash, jsonify, make_response
from RygolGosan import app, bcrypt, db, forms, models, api
from RygolGosan.forms import RegistrationForm, LoginForm
from RygolGosan.models import User, Post
from flask import session as login_session
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'RygolGosan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 1, 2021'
    },
    {
        'author': 'RygolGosan',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'October 1, 2021'
    }
]



''' Public User Accessible Routes '''
# Primary Page Access for Logged In or Public Users depending on Session Status
# Routes to the Home Page/Primary Index of the Site
@app.route('/')
@app.route('/home')
def home():
    if 'username' not in login_session:
        return render_template('publicindex.html', posts=posts)
    else:
        return render_template('index.html', posts=posts)

# Features Page Access
@app.route('/features')
def features():
    return render_template('features.html')

# Getting Started Page Access
@app.route('/getting-started')
def gettingstarted():
    return render_template('gettingstarted.html')

# Registration Page Access
@app.route('/signup', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
#    else:
#        flash('Registration Unsuccessful. The username may already be taken', 'danger')
    return render_template('signup.html', title='Sign Up', form=form)

# Login Page Access
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Login Successful!', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)



''' Logged In Account User Accessible Routes '''
# Logout Page Access if logged in on site
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Account Page Access for users that are logged in with valid credentials
@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

# Dashboard Page Access for admin users that are logged in with valid credentials and security clearances
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', title='Dashboard')