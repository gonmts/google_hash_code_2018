from read_file import *
from listFunctions import *
from cTrip import *
from cCar import *


filename = ""

rows, columns, bonus, time, ride_list, car_list = read_file(filename)
MAX_CAR_PROCESS = min(50, len(car_list))

sortedTrips = sorted(ride_list, key=cTrip.getLatestStart)

class main:

	def __init__(self):
		pass

	def main(self):
		for trip in sortedTrips:
			startIndex = getRandomListIndex(car_list, MAX_CAR_PROCESS)
			maxScore = 0
			maxIndex = -1
			for i in range(startIndex, MAX_CAR_PROCESS + startIndex)
				
