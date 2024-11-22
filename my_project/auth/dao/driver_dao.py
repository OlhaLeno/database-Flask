# для бекенду
from my_project.db_init import db
from my_project.auth.models.driver import Driver

class DriverDAO:
    def get_all(self):
        return Driver.query.all()

    def get_by_id(self, driver_id):
        return Driver.query.get(driver_id)

    def create(self, data):
        new_driver = Driver(**data)
        db.session.add(new_driver)
        db.session.commit()
        return new_driver

    def update(self, driver_id, data):
        driver = Driver.query.get(driver_id)
        if driver:
            for key, value in data.items():
                setattr(driver, key, value)
            db.session.commit()
            return driver
        return None

    def delete(self, driver_id):
        driver = Driver.query.get(driver_id)
        if driver:
            db.session.delete(driver)
            db.session.commit()
            return True
        return False
