from my_project.db_init import db

class Driver(db.Model):
    __tablename__ = 'driver'

    driver_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False)
    license_number = db.Column(db.String(45), nullable=False)
    experience_years = db.Column(db.String(45), nullable=False)
    phone_number = db.Column(db.String(14), nullable=False)

    def to_dict(self):
        return {
            'driver_id': self.driver_id,
            'name': self.name,
            'license_number': self.license_number,
            'experience_years': self.experience_years,
            'phone_number': self.phone_number
        }
