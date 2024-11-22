from my_project.auth.dao.driver_dao import DriverDAO

class DriverService:
    def __init__(self):
        self.driver_dao = DriverDAO()

    def get_all_drivers(self):
        return self.driver_dao.get_all()

    def get_driver_by_id(self, driver_id):
        return self.driver_dao.get_by_id(driver_id)

    def create_driver(self, data):
        return self.driver_dao.create(data)

    def update_driver(self, driver_id, data):
        return self.driver_dao.update(driver_id, data)

    def delete_driver(self, driver_id):
        return self.driver_dao.delete(driver_id)
