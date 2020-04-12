from flask import Blueprint

error_blueprint = Blueprint('error_blueprint',__name__)

from app.errors import handlers 
# Doing this import so that the error handlers in it are registered with the blueprint