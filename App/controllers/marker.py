from App.models import Marker
from App.database import db


def create_marker():
    new_marker = Marker()
    db.session.add(new_marker)
    db.session.commit()
    return new_marker