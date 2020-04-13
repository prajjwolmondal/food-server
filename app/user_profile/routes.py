from app.user_profile import user_profile_blueprint
from app import db
from app.models import User
from app.user_profile.forms import AdditionalInfoForm
from flask import render_template, session, redirect, url_for
from flask_login import login_required

@user_profile_blueprint.route('/user_profile')
@login_required
def get_user_profile():
    db_user_object = db.get_user_by_id(session['userID'])
    user = User(db_user_object['username'], db_user_object['password'], db_user_object['_id'], db_user_object['email'])
    return render_template('user_profile/user_profile.html', user=user)

@user_profile_blueprint.route('/user/additional_info', methods=["GET", "POST"])
def get_additional_info():
    form = AdditionalInfoForm()
    if form.validate_on_submit():
        db.update_user_preferences(session['userID'], {'postal_code': form.postal_code.data, 
                                    'cuisine_preferences': form.cuisine_preferences.data})
        session['user_postal_code'] = form.postal_code.data
        return redirect(url_for('main_blueprint.index'))
    return render_template('user_profile/additional_info.html', form=form)