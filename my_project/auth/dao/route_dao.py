from my_project.db_init import db
from my_project.auth.models.route import Route

class RouteDAO:
    def get_all(self):
        return Route.query.all()

    def get_by_id(self, route_id):
        return Route.query.get(route_id)

    def create(self, data):
        new_route = Route(**data)
        db.session.add(new_route)
        db.session.commit()
        return new_route

    def update(self, route_id, data):
        route = Route.query.get(route_id)
        if route:
            for key, value in data.items():
                setattr(route, key, value)
            db.session.commit()
            return route
        return None

    def delete(self, route_id):
        route = Route.query.get(route_id)
        if route:
            db.session.delete(route)
            db.session.commit()
            return True
        return False
