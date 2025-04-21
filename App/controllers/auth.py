from flask import g
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from App.models import User  # Adjust based on your app's model import

def add_auth_context(app):
    @app.before_request
    def load_current_user():
        """
        Load the current user for each request based on JWT.
        """
        try:
            verify_jwt_in_request()  # Verify JWT is present in the request
            username = get_jwt_identity()  # Get the username from the JWT
            g.current_user = User.query.filter_by(username=username).first()  # Query the user by username
        except Exception as e:
            g.current_user = None  # If no JWT or error, set current_user to None
            print(f"Error loading current user: {e}")

    @app.context_processor
    def inject_user():
        """
        Inject 'is_authenticated' and 'current_user' into the templates.
        """
        is_authenticated = g.current_user is not None  # Check if a user is loaded
        return dict(is_authenticated=is_authenticated, current_user=g.current_user)
