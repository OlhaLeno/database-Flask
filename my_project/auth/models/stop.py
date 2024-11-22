from my_project.db_init import db

class Stop(db.Model):
    __tablename__ = 'stop'

    stop_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    route_stops = db.relationship('RouteStop', back_populates='stop')
    def to_dict(self):
        return {
            'stop_id': self.stop_id,
            'name': self.name,
            'address': self.address
        }
