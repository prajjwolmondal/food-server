from flask import Flask
from config import Config
from flask_bcrypt  import Bcrypt
from flask_login import LoginManager
from app.db import DB

application = Flask(__name__)
application.config.from_object(Config)
bcrypt = Bcrypt(application)
login = LoginManager(application)
login.login_view = 'login'
# The 'login' value above is the function (or endpoint) name for the login view. 
# In other words, the name you would use in a url_for() call to get the URL.
db = DB(application)

from app import routes, models, errors