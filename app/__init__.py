from flask import Flask
from config import Config
from flask_bcrypt  import Bcrypt
from flask_login import LoginManager
from app.db import DB
from app.errors import error_blueprint


application = Flask(__name__)
application.config.from_object(Config)
application.register_blueprint(error_blueprint)
bcrypt = Bcrypt(application)
login = LoginManager(application)
login.login_view = 'auth_blueprint.login'
# The 'login' value above is the function (or endpoint) name for the login view. 
# In other words, the name you would use in a url_for() call to get the URL.
db = DB(application)

from app.auth import auth_blueprint
application.register_blueprint(auth_blueprint, url_prefix="/auth")

from app.main import main_blueprint
application.register_blueprint(main_blueprint)

from app import models