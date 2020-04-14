from app.main import main_blueprint
from app.main.forms import SearchForm
from flask import render_template, redirect, send_from_directory, session, url_for

import os

@main_blueprint.route('/', methods=['GET', 'POST'])
@main_blueprint.route('/index', methods=['GET', 'POST'])
def index():
     form = SearchForm()
     if form.validate_on_submit():
          session['searchQuery'] = form.search_query.data
          return redirect(url_for('data_sources_blueprint.get_restaurant_from_google'))
     return render_template('index.html', title="Home Page", form=form)

@main_blueprint.route('/favicon.ico')
def favicon():
     return send_from_directory('templates', 'favicon.ico', mimetype='image/vnd.microsoft.icon')
