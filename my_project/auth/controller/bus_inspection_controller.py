# controllers/bus_inspection_controller.py
from flask import request, jsonify
from my_project.auth.service.bus_inspection_service import BusInspectionService

bus_inspection_service = BusInspectionService()

def get_all_inspections():
    inspections = bus_inspection_service.get_all_inspections()
    return jsonify([inspection.to_dict() for inspection in inspections]), 200

def get_inspection_by_id(inspection_id):
    inspection = bus_inspection_service.get_inspection_by_id(inspection_id)
    if inspection:
        return jsonify(inspection.to_dict()), 200
    return jsonify({'message': 'Inspection not found'}), 404

def create_bus_inspection():
    data = request.json
    try:
        new_inspection = bus_inspection_service.create_bus_inspection(data)
        return jsonify(new_inspection.to_dict()), 201
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

def update_bus_inspection(inspection_id):
    data = request.json
    updated_inspection = bus_inspection_service.update_bus_inspection(inspection_id, data)
    if updated_inspection:
        return jsonify(updated_inspection.to_dict()), 200
    return jsonify({'message': 'Inspection not found'}), 404

def delete_bus_inspection(inspection_id):
    success = bus_inspection_service.delete_bus_inspection(inspection_id)
    if success:
        return jsonify({'message': 'Inspection deleted successfully'}), 200
    return jsonify({'message': 'Inspection not found'}), 404

def get_inspections_by_bus_id(bus_id):
    inspections = bus_inspection_service.get_inspections_by_bus_id(bus_id)
    return jsonify([inspection.to_dict() for inspection in inspections]), 200


def create_bus_inspection():
    data = request.get_json()

    # Отримуємо дані з запиту
    bus_id = data.get('bus_id')
    inspection_date = data.get('inspection_date')
    inspection_result = data.get('inspection_result')
    remarks = data.get('remarks')

    if not bus_id or not inspection_date or not inspection_result:
        return jsonify({"message": "Missing required fields"}), 400

    try:
        bus_inspection_service.create_inspection(bus_id, inspection_date, inspection_result, remarks)
        return jsonify({"message": "Bus inspection record created successfully"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500