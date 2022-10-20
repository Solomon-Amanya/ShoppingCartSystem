class Floors:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots_per_floor = 50
        self.no_of_floors = 10
        self.total_number_of_spots = self.spots_per_floor * self.no_of_floors
        self.availableSpots = []

        # Check available spots on a floor
        for floor_number in range(self.no_of_floors):
            for i in range(self.spots_per_floor):
                return i

    # Park vehicle if spot is available
    def park(self, car):
        for spot in self.availableSpots:
            if spot.park(car):
                return True
            else:
                print("Please open parking on the next floor.")
        return False

    # Remove vehicle from a spot
    def retrieve(self, car):
        for spot in self.availableSpots:
            if spot.get_car(car) == car:
                spot.retreive_car(car)
                return True
        return False

    def __repr__(self):
        return self.floor_number
