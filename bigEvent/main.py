from read_file import *
from listFunctions import *
from cTrip import *
from cCar import *
import sys


filename_input = "datasets/a_example.in"
filename_output = "output_1.out"

rows, columns, bonus, time, ride_list, car_list = read_file(filename)
MAX_CAR_PROCESS = min(50, len(car_list))
CLEAN_TRIPS = True

sortedTrips = sorted(ride_list, key=cTrip.getLatestStart)

class main:

    def __init__(self):
        pass

    def main(self):
        trips_taken = []
        for t in time:
    		for i in range(0, len(sortedTrips)):
                trip = sortedTrips[i]
    			startIndex = getRandomListIndex(car_list, MAX_CAR_PROCESS)

                min_cost = sys.maxsize
                selected_car = None
                for i in range(startIndex, MAX_CAR_PROCESS + startIndex):
                    if car_list[i].isValid(trip, t):
                        cost = car_list[i].score(trip, t)
                        if (cost < min_cost):
                            min_cost = cost
                            selected_car = car_list[i]

                if (selected_car is not None):
                    selected_car.beginTrip(trip)
                    trips_taken += [i]

            for index in range(1, len(trips_taken) + 1):
                del sortedTrips[-index]

        write_file(filename_output, car_list)
