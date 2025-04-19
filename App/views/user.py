from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views
from App.controllers.marker import *
from App.controllers.user import create_marker,delete_marker

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
@jwt_required()
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@user_views.route('/users', methods=['POST'])
@jwt_required()
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))


@user_views.route('/editmap', methods=['GET'])
@jwt_required()
def editmap_page():
    markers = get_all_markers_json()
    return render_template('editmap.html',markers=markers)

@user_views.route('/editmap', methods=['POST'])
@jwt_required()
def editmap_action():
    data = request.form
    flash(f"Marker {data['name']} created!")
    create_marker(data['name'], data['latitude'], data['longitude'], data['faculty'], jwt_current_user.id)
    return redirect(url_for('user_views.editmap_page'))

@user_views.route('/deletemarker', methods=['POST'])
@jwt_required()
def deletemap_action():
    marker_id = request.form['marker_id']
    if marker_id:
        delete_marker(marker_id)
        flash(f"Marker {marker_id} deleted!")
    else:
        flash("Marker ID not provided!")
    return redirect(url_for('user_views.editmap_page'))