from App.models import User,Marker
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
def create_marker(name, lat, long, faculty, user_id):
    new_marker = Marker(name, lat, long, faculty, user_id)
    db.session.add(new_marker)
    db.session.commit()
    return new_marker

def delete_marker(id):
    marker = Marker.query.get(id)
    if marker:
        db.session.delete(marker)
        db.session.commit()
        return True
    return False