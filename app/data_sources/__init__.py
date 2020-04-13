from flask import Blueprint

data_sources_blueprint = Blueprint("data_sources_blueprint", __name__)

from app.data_sources import routes