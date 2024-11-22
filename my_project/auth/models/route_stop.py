from my_project.db_init import db

class RouteStop(db.Model):
    __tablename__ = 'route_stop'

    route_stop_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route_id = db.Column(db.Integer, db.ForeignKey('route.route_id'), nullable=False)
    stop_id = db.Column(db.Integer, db.ForeignKey('stop.stop_id'), nullable=False)
    sequence = db.Column(db.String(45), nullable=False)
    distance_from_previous = db.Column(db.String(45), nullable=False)
    price_from_previous = db.Column(db.String(45), nullable=False)


    route = db.relationship('Route', back_populates='route_stops')
    stop = db.relationship('Stop', back_populates='route_stops')
    def to_dict(self):
        return {
            'route_stop_id': self.route_stop_id,
            'route_id': self.route_id,
            'stop_id': self.stop_id,
            'sequence': self.sequence,
            'distance_from_previous': self.distance_from_previous,
            'price_from_previous': self.price_from_previous
        }
