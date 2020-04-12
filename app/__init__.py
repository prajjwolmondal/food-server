from app.db import DB
from app.errors import error_blueprint
from config import Config
from flask import Flask
from flask_bcrypt  import Bcrypt
from flask_login import LoginManager
from logging.handlers import RotatingFileHandler

import logging
import os

bcrypt = Bcrypt()
login = LoginManager()
login.login_view = 'auth_blueprint.login'
# The 'login' value above is the function (or endpoint) name for the login view. 
# In other words, the name you would use in a url_for() call to get the URL.
db = DB()

def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)
    application.register_blueprint(error_blueprint)

    bcrypt.init_app(application)
    login.init_app(application)
    db.set_pymongo_context(application)

    from app.auth import auth_blueprint
    application.register_blueprint(auth_blueprint, url_prefix="/auth")

    from app.main import main_blueprint
    application.register_blueprint(main_blueprint)

    from app.user_profile import user_profile_blueprint
    application.register_blueprint(user_profile_blueprint)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/foodserver.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    application.logger.addHandler(file_handler)
    application.logger.setLevel(logging.INFO)
    application.logger.info('foodserver starting up')

    return application

from app import models