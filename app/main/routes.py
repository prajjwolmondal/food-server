from app.main import main_blueprint
from app.main.forms import SearchForm, SurpriseForm
from flask import render_template, redirect, send_from_directory, session, url_for

import os

@main_blueprint.route('/', methods=['GET', 'POST'])
@main_blueprint.route('/index', methods=['GET', 'POST'])
def index():
     search_form = SearchForm()
     surprise_form = SurpriseForm()
     if search_form.validate_on_submit():
          session.pop('searchQuery', None)
          session['searchQuery'] = search_form.search_query.data
          return redirect(url_for('data_sources_blueprint.get_restaurant_from_google'))
     return render_template('index.html', title="Home Page", form=search_form, surprise_form=surprise_form)

@main_blueprint.route('/suprise', methods=['POST'])
def surprise():
     return redirect(url_for('data_sources_blueprint.surprise_me'))

@main_blueprint.route('/favicon.ico')
def favicon():
     return send_from_directory('templates', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

# TODO: Fix bug of "Surprise me" triggering the field required validation for search