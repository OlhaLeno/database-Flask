from flask import request, jsonify
from my_project.auth.service.route_service import RouteService

route_service = RouteService()

def get_all_routes():
    routes = route_service.get_all_routes()
    return jsonify([route.to_dict() for route in routes]), 200

def get_route_by_id(route_id):
    route = route_service.get_route_by_id(route_id)
    if route:
        return jsonify(route.to_dict()), 200
    return jsonify({'message': 'Route not found'}), 404

def create_route():
    data = request.json
    new_route = route_service.create_route(data)
    return jsonify(new_route.to_dict()), 201

def update_route(route_id):
    data = request.json
    updated_route = route_service.update_route(route_id, data)
    if updated_route:
        return jsonify(updated_route.to_dict()), 200
    return jsonify({'message': 'Route not found'}), 404

def delete_route(route_id):
    success = route_service.delete_route(route_id)
    if success:
        return jsonify({'message': 'Route deleted successfully'}), 200
    return jsonify({'message': 'Route not found'}), 404

def insert_route_entries():
    response, status_code = route_service.insert_route_entries()
    return jsonify(response), status_code