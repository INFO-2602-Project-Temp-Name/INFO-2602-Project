from .user import create_user,create_marker
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_marker('uwi1',10.6398,-61.3997,'Engineering',1)
    create_marker('uwi2',10.6394,-61.3993,'Engineering',1)
    create_marker('uwi3',10.6390,-61.3990,'Engineering',1)

