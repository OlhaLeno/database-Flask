# models/bus.py

from my_project.db_init import db

class Bus(db.Model):
    __tablename__ = 'bus'

    bus_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    manufacturer = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.String(100), nullable=False)
    age = db.Column(db.String(45), nullable=False)
    mileage = db.Column(db.String(100), nullable=False)
    ownership_type = db.Column(db.String(100), nullable=False)


    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'), nullable=True)


    route = db.relationship('Route', back_populates='buses')

    def to_dict(self):
        return {
            'bus_id': self.bus_id,
            'manufacturer': self.manufacturer,
            'capacity': self.capacity,
            'age': self.age,
            'mileage': self.mileage,
            'ownership_type': self.ownership_type,
            'route_id': self.route_id,

        }
