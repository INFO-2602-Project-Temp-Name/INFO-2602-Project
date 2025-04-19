from .user import create_user,create_marker
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    create_marker('UWI SPEC',10.6404,-61.3957,'Sport',1)
    create_marker('TLC',10.6415,-61.3967,'Other',1)
    create_marker('UWI Food Court',10.63895,-61.3983,'Other',1)
    create_marker('Alma Jordan Library',10.6395,-61.3989,'Other',1)

