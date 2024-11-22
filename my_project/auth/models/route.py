from my_project.db_init import db


class Route(db.Model):
    __tablename__ = 'route'

    route_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_address = db.Column(db.String(200), nullable=False)
    end_address = db.Column(db.String(200), nullable=False)
    total_distance = db.Column(db.String(45), nullable=False)
    ticket_price = db.Column(db.String(45), nullable=False)


    buses = db.relationship('Bus', back_populates='route', cascade='all, delete-orphan')
    route_stops = db.relationship('RouteStop', back_populates='route')
    def to_dict(self):
        return {
            'route_id': self.route_id,
            'start_address': self.start_address,
            'end_address': self.end_address,
            'total_distance': self.total_distance,
            'ticket_price': self.ticket_price,
            'stops': [rs.stop.to_dict() for rs in self.route_stops]

        }
