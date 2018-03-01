from read_file import *
from listFunctions import *
from cTrip import *
from cCar import *
from tqdm import tqdm
import sys

class main:

	def __init__(self):
		pass

	def main(self):
		for f_index in range(5):
			in_files = ["a_example", "b_should_be_easy", "c_no_hurry", "d_metropolis", "e_high_bonus"]
			out_files = ["a_out", "b_out", "c_out", "d_out", "e_out"]

			filename_input = "datasets/" +  in_files[f_index] + ".in"
			filename_output = in_files[f_index] + ".out"
			rows, columns, bonus, time, ride_list, car_list = read_ride_file(filename_input)

			MAX_CAR_PROCESS = len(car_list)
			if(f_index == 4):
				MAX_CAR_PROCESS = min(100, len(car_list))
			#sortedTrips = sorted(ride_list, key=cTrip.getLatestStart)
			sortedTrips = sorted(ride_list, key=cTrip.getLatestStart)

			trips_taken = []
			for t in tqdm(range(time)):
				for i in range(0, len(sortedTrips)):
					trip = sortedTrips[i]
					startIndex = getRandomListIndex(car_list, MAX_CAR_PROCESS)

					min_cost = sys.maxsize
					selected_car = None
					for k in range(startIndex, MAX_CAR_PROCESS + startIndex):
						if car_list[k].isValid(trip, t):
							cost = car_list[k].score(trip, t)
							if (cost < min_cost):
								min_cost = cost
								selected_car = car_list[k]

					if (selected_car is not None):
						selected_car.beginTrip(trip, t)
						trips_taken += [i]

				for i in range(1, len(trips_taken) + 1):
					index_to_del =  trips_taken[-i]
					del sortedTrips[index_to_del]
				trips_taken = []

			write_file(filename_output, car_list)

main().main()
