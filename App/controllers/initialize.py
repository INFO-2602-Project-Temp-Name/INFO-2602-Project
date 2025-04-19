from .user import create_user,create_marker
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_marker('Eng',10.6398,-61.3997,'Engineering',1)
    create_marker('FST',10.6394,-61.3993,'Science and Technology',1)
    create_marker('Law',10.6390,-61.3990,'Law',1)

