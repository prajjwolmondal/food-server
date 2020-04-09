from flask import render_template
from app.errors import error_blueprint

@error_blueprint.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404