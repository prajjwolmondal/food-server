from app import application, bcrypt, db
from app.models import User
from app.forms import LoginForm, SignupForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@application.route('/')
@application.route('/index')
def index():
     return render_template('index.html', title="Home Page")

@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        db_user_object = db.get_user_by_username(form.username.data)
        if db_user_object is None:
            flash('Invalid username or password')
            return redirect(url_for('login'))
        user = User(db_user_object['username'], db_user_object['password'], db_user_object['_id'], db_user_object['email'])
        if not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)

        # An attacker could insert a URL to a malicious site in the next argument, so the application only redirects
        # when the URL is relative, which ensures that the redirect stays within the same site as the application. 
        # To determine if the URL is relative or absolute, I parse it with Werkzeug's url_parse() function 
        # and then check if the netloc component is set or not.
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Log in", form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@application.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        encrypted_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        print(f"encrypted_pwd: {encrypted_pwd}")
        db.add_user({'username': form.username.data, 'password': str(encrypted_pwd), 'email': form.email.data})
        return redirect(url_for('index'))
    return render_template('signup.html', title="Sign in", form=form)

@application.route('/user/<username>')
@login_required
def get_user_profile(username):
    db_user_object = db.get_user_by_username(username)
    user = User(db_user_object['username'], db_user_object['password'], db_user_object['_id'], db_user_object['email'])
    return render_template('user_profile.html', user=user)
