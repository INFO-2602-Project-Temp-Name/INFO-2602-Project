from App.models import Marker
from App.database import db


def get_all_markers():
    return Marker.query.all()

def get_all_markers_json():
    markers = get_all_markers()
    if not markers:
        return []
    json_markers = [marker.get_json() for marker in markers]
    return json_markers