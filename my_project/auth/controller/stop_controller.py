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
    if isinstance(new_stop, dict) and 'error' in new_stop:
        return jsonify(new_stop), 400
    return jsonify({'message': 'stop added successfully'}), 201

def update_stop(stop_id):
    data = request.json
    result= stop_service.update_stop(stop_id, data)
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), 400  # Повертаємо помилку тригера
    if result:
        return jsonify({'message': 'stop updated successfully', 'stop': result.to_dict()}), 200
    return jsonify({'message': 'stop not found'}), 404

def delete_stop(stop_id):
    result = stop_service.delete_stop(stop_id)
    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), 400
    if result:
        return jsonify({'message': 'stop deleted successfully'}), 200
    return jsonify({'message': 'stop not found'}), 404

