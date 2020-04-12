from flask import Blueprint

user_profile_blueprint = Blueprint('user_profile_blueprint', __name__)

from app.user_profile import routes