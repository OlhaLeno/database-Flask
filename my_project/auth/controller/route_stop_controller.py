from flask import request, jsonify
from my_project.auth.service.route_stop_service import RouteStopService

route_stop_service = RouteStopService()

def get_all_route_stops():
    route_stops = route_stop_service.get_all_route_stops()
    return jsonify([route_stop.to_dict() for route_stop in route_stops]), 200

def get_route_stops_by_route(route_id):
    route_stops = route_stop_service.get_route_stops_by_route(route_id)
    return jsonify([rs.stop.to_dict() for rs in route_stops]), 200

def get_route_stop_by_id(route_stop_id):
    route_stop = route_stop_service.get_route_stop_by_id(route_stop_id)
    if route_stop:
        return jsonify(route_stop.to_dict()), 200
    return jsonify({'message': 'Route Stop not found'}), 404

def create_route_stop():
    data = request.json
    new_route_stop = route_stop_service.create_route_stop(data)
    return jsonify(new_route_stop.to_dict()), 201

def update_route_stop(route_stop_id):
    data = request.json
    updated_route_stop = route_stop_service.update_route_stop(route_stop_id, data)
    if updated_route_stop:
        return jsonify(updated_route_stop.to_dict()), 200
    return jsonify({'message': 'Route Stop not found'}), 404

def delete_route_stop(route_stop_id):
    success = route_stop_service.delete_route_stop(route_stop_id)
    if success:
        return jsonify({'message': 'Route Stop deleted successfully'}), 200
    return jsonify({'message': 'Route Stop not found'}), 404
