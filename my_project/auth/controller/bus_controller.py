from flask import request, jsonify
from my_project.auth.service.bus_service import BusService

bus_service = BusService()

def get_all_buses():
    buses = bus_service.get_all_buses()
    return jsonify([bus.to_dict() for bus in buses]), 200

def get_bus_by_id(bus_id):
    bus = bus_service.get_bus_by_id(bus_id)
    if bus:
        return jsonify(bus.to_dict()), 200
    return jsonify({'message': 'Bus not found'}), 404

def create_bus():
    data = request.json
    new_bus = bus_service.create_bus(data)
    return jsonify(new_bus.to_dict()), 201

def update_bus(bus_id):
    data = request.json
    updated_bus = bus_service.update_bus(bus_id, data)
    if updated_bus:
        return jsonify(updated_bus.to_dict()), 200
    return jsonify({'message': 'Bus not found'}), 404

def delete_bus(bus_id):
    success = bus_service.delete_bus(bus_id)
    if success:
        return jsonify({'message': 'Bus deleted successfully'}), 200
    return jsonify({'message': 'Bus not found'}), 404

def get_buses_by_route(route_id):

    buses = bus_service.get_buses_by_route(route_id)
    return jsonify([bus.to_dict() for bus in buses]), 200