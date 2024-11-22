from flask import request, jsonify
from my_project.auth.service.stop_service import StopService

stop_service = StopService()

def get_all_stops():
    stops = stop_service.get_all_stops()
    return jsonify([stop.to_dict() for stop in stops]), 200

def get_stop_by_id(stop_id):
    stop = stop_service.get_stop_by_id(stop_id)
    if stop:
        return jsonify(stop.to_dict()), 200
    return jsonify({'message': 'Stop not found'}), 404

def create_stop():
    data = request.json
    new_stop = stop_service.create_stop(data)
    return jsonify(new_stop.to_dict()), 201

def update_stop(stop_id):
    data = request.json
    updated_stop = stop_service.update_stop(stop_id, data)
    if updated_stop:
        return jsonify(updated_stop.to_dict()), 200
    return jsonify({'message': 'Stop not found'}), 404

def delete_stop(stop_id):
    success = stop_service.delete_stop(stop_id)
    if success:
        return jsonify({'message': 'Stop deleted successfully'}), 200
    return jsonify({'message': 'Stop not found'}), 404
