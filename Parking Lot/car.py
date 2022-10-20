class Car:
    def __init__(self, license_plate, company_name, type_of_car):
        self.license_plate = license_plate
        self.company_name = company_name
        self.type_of_vehicle = type_of_car

    def __repr__(self):
        return self.license_plate
