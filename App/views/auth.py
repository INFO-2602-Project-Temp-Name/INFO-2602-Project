from flask import Blueprint, make_response, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from App.controllers.user import get_all_users


from.index import index_views
from .user import user_views

from App.controllers import (
    login
)

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')




'''
Page/Action Routes
'''    
@auth_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

@auth_views.route('/identify', methods=['GET'])
@jwt_required()
def identify_page():
    return render_template('message.html', title="Identify", message=f"You are logged in as {current_user.id} - {current_user.username}")
    

@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    token = login(data['username'], data['password'])

    if not token:
        flash('Bad username or password given', 'error')
        return redirect(request.referrer)

    # response = redirect(request.referrer)
    #testing start
    response = make_response(f"""
        <h2>Logged in.</h2>
        <p>access_token set. Token = {token}</p>
        <a href="/">Go to map</a>
    """)
    #testing end
    # response = redirect(url_for('user_views.editmap_page'))
    set_access_cookies(response, token)
    flash('Login Successful', 'success')
    return response

@auth_views.route('/logout', methods=['GET'])
def logout_action():
    response = redirect(request.referrer) 
    flash("Logged Out!")
    unset_jwt_cookies(response)
    return response

