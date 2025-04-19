from App.database import db

class Marker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    faculty = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, latitude, longitude, faculty, user_id):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.faculty = faculty
        self.user_id = user_id
        
    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'faculty': self.faculty,
            'user_id': self.user_id
        }

    def __repr__(self):
        return f"<Marker {self.name} lat:({self.latitude}, long:{self.longitude})> category: {self.faculty}"