from my_project.db_init import db
from my_project.auth.models.bus import Bus

class BusDAO:
    def get_all(self):
        return Bus.query.all()

    def get_by_id(self, bus_id):
        return Bus.query.get(bus_id)

    def create(self, data):
        new_bus = Bus(**data)
        db.session.add(new_bus)
        db.session.commit()
        return new_bus

    def update(self, bus_id, data):
        bus = Bus.query.get(bus_id)
        if bus:
            for key, value in data.items():
                setattr(bus, key, value)
            db.session.commit()
            return bus
        return None

    def delete(self, bus_id):
        bus = Bus.query.get(bus_id)
        if bus:
            db.session.delete(bus)
            db.session.commit()
            return True
        return False

    def get_buses_by_route(self, route_id):

        return Bus.query.filter_by(route_id=route_id).all()