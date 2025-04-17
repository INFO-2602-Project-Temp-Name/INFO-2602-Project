from App.database import db
from App.models.user import User

class Admin(User):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, username, password):
        pass

    def __repr__(self):
        pass