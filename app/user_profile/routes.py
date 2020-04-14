from app import db
from app.data_sources import utils
from app.models import User
from app.user_profile import user_profile_blueprint
from app.user_profile.forms import AdditionalInfoForm
from flask import render_template, session, redirect, url_for
from flask_login import login_required

@user_profile_blueprint.route('/user_profile')
@login_required
def get_user_profile():
    user_instance = session['userInstance']
    db_user_object = db.get_user_by_id(user_instance['id'])
    user = User(db_user_object['username'], db_user_object['password'], db_user_object['_id'], db_user_object['email'])
    return render_template('user_profile/user_profile.html', user=user)

@user_profile_blueprint.route('/user/additional_info', methods=["GET", "POST"])
def get_additional_info():
    form = AdditionalInfoForm()
    user_instance = session['userInstance']
    if form.validate_on_submit():
        user_lat_long = utils.convert_postal_code_to_latlong(form.postal_code.data)
        db.update_user_preferences(user_instance['id'], {'postal_code': form.postal_code.data,
                                    'lat_long': user_lat_long, 'cuisine_preferences': form.cuisine_preferences.data})
        user_instance['postal_code'] = form.postal_code.data
        user_instance['lat_long'] = user_lat_long
        user_instance['cuisine_preferences'] = form.cuisine_preferences.data
        session['userInstance'] = user_instance
        return redirect(url_for('main_blueprint.index'))
    print(f"user_instance: {user_instance}")
    return render_template('user_profile/additional_info.html', form=form)