from flask import Blueprint, render_template

home_views = Blueprint('home_views', __name__)

@home_views.route('/')
def homepage():
    return render_template('home.html')
