from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views
from App.controllers.marker import *

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required
)

map_views = Blueprint('map_views', __name__, template_folder='../templates')

@map_views.route('/map', methods=['GET'])
def map_page():
    markers = get_all_markers_json()
    return render_template('map.html',markers = markers)