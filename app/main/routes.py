from app.main import main_blueprint
from app.main.forms import SearchForm
from flask import render_template, redirect, session, url_for

@main_blueprint.route('/', methods=['GET', 'POST'])
@main_blueprint.route('/index', methods=['GET', 'POST'])
def index():
     form = SearchForm()
     if form.validate_on_submit():
          session['searchQuery'] = form.search_query.data
          return redirect(url_for('data_sources_blueprint.get_restaurant_from_google'))
     return render_template('index.html', title="Home Page", form=form)