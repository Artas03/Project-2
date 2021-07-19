from application import db

class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    mot = db.Column(db.String(50), nullable=False)
