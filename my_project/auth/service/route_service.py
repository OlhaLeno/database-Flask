from my_project.auth.dao.route_dao import RouteDAO

class RouteService:
    def __init__(self):
        self.route_dao = RouteDAO()

    def get_all_routes(self):
        return self.route_dao.get_all()

    def get_route_by_id(self, route_id):
        return self.route_dao.get_by_id(route_id)

    def create_route(self, data):
        return self.route_dao.create(data)

    def update_route(self, route_id, data):
        return self.route_dao.update(route_id, data)

    def delete_route(self, route_id):
        return self.route_dao.delete(route_id)
