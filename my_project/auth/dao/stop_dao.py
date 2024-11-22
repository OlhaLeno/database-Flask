from my_project.db_init import db
from my_project.auth.models.stop import Stop

class StopDAO:
    def get_all(self):
        return Stop.query.all()

    def get_by_id(self, stop_id):
        return Stop.query.get(stop_id)

    def create(self, data):
        new_stop = Stop(**data)
        db.session.add(new_stop)
        db.session.commit()
        return new_stop

    def update(self, stop_id, data):
        stop = Stop.query.get(stop_id)
        if stop:
            for key, value in data.items():
                setattr(stop, key, value)
            db.session.commit()
            return stop
        return None

    def delete(self, stop_id):
        stop = Stop.query.get(stop_id)
        if stop:
            db.session.delete(stop)
            db.session.commit()
            return True
        return False
