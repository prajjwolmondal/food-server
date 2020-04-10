from app import db
from app.main import main_blueprint
from app.models import User
from flask import render_template
from flask_login import login_required

@main_blueprint.route('/')
@main_blueprint.route('/index')
def index():
     return render_template('index.html', title="Home Page")

@main_blueprint.route('/user/<username>')
@login_required
def get_user_profile(username):
    db_user_object = db.get_user_by_username(username)
    user = User(db_user_object['username'], db_user_object['password'], db_user_object['_id'], db_user_object['email'])
    return render_template('user_profile.html', user=user)
