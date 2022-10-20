class Spots:
    def __init__(self, spot_number, type_of_car):
        # self.floor = floor
        self.spot_number = spot_number
        self.car = None
        self.type_of_car = type_of_car

    def is_available(self):
        self.car = None
        return self.car

    def park(self, car):
        if car.type_of_car == self.type_of_car:
            self.car = car
            return True
        else:
            return False

    def retrieve_car(self):
        self.car = None
        return self.car

    def get_car(self):
        return self.car

    def __repr__(self):
        return self.type_of_car
