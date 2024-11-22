from flask import request, jsonify
from my_project.auth.service.driver_service import DriverService

driver_service = DriverService()

def get_all_drivers():
    drivers = driver_service.get_all_drivers()
    return jsonify([driver.to_dict() for driver in drivers]), 200

def get_driver_by_id(driver_id):
    driver = driver_service.get_driver_by_id(driver_id)
    if driver:
        return jsonify(driver.to_dict()), 200
    return jsonify({'message': 'Driver not found'}), 404

def create_driver():
    data = request.json
    new_driver = driver_service.create_driver(data)
    return jsonify(new_driver.to_dict()), 201

def update_driver(driver_id):
    data = request.json
    updated_driver = driver_service.update_driver(driver_id, data)
    if updated_driver:
        return jsonify(updated_driver.to_dict()), 200
    return jsonify({'message': 'Driver not found'}), 404

def delete_driver(driver_id):
    success = driver_service.delete_driver(driver_id)
    if success:
        return jsonify({'message': 'Driver deleted successfully'}), 200
    return jsonify({'message': 'Driver not found'}), 404
