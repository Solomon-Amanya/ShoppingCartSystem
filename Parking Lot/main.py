from car import Car
from spots import Spots
from floor import Floors

car1 = Car("UBF 485D", "Toyota", "Mark X")
car2 = Car("UAF 465F", "Range Rover", "Sport")
car3 = Car("UBD 746H", "Mercedes Benz", "AMG BlueTec")

spot = Spots(1, car1)

#floor = Floors("1")
#floor.availableSpots.append(car1)
#floor.availableSpots.append(car2)
#floor.availableSpots.append(car3)

print(str(spot))

