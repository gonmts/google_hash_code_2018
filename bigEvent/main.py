from read_file import *
from cTrip import *
from cCar import *


filename = ""
rows, columns, bonus, time, ride_list, car_list = read_file(filename)

sortedElements = sorted(ride_list, key=cTrip.getLatestStart)