# why Python is great: namedtuples
# using namedtuple is way shorter than defining a class manually

from collections import namedtuple

Car = namedtuple('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color # red
my_car.mileage # 3812.4

my_car # Car(color='red', mileage=3812.4)

# Like tuples, namedtuples are immutables:
my_car.color = 'blue' # error