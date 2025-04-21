import os
from flask import Flask, render_template
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.middleware.proxy_fix import ProxyFix
from werkzeug.datastructures import  FileStorage


from App.database import init_db
from App.config import load_config


from App.controllers import (
    setup_jwt,
    add_auth_context
)

from App.views import views, setup_admin

def add_views(app):
    for view in views:
        app.register_blueprint(view)

def create_app(overrides={}):
    app = Flask(__name__, static_url_path='/static')
    load_config(app, overrides)
    CORS(app)
    add_auth_context(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    init_db(app)
    jwt = setup_jwt(app)
    setup_admin(app)
    @jwt.invalid_token_loader
    @jwt.unauthorized_loader
    def custom_unauthorized_response(error):
        return render_template('401.html', error=error), 401
    #testing start
    from flask_jwt_extended import verify_jwt_in_request_optional, get_jwt_identity
    @app.context_processor
    def inject_user():
        try:
            verify_jwt_in_request_optional()
            user_id = get_jwt_identity()
            print(f"[Context Processor] Logged in as user ID: {user_id}")
            return {'logged_in_user_id': user_id}
        except Exception as e:
            print("[Context Processor] JWT missing or invalid:", e)
            return {'logged_in_user_id': None}
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)
    #testing end
    app.app_context().push()
    return app