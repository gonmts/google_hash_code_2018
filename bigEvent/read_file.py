from cCar import *
from cTrip import *

def distance(start, finish):
    startX, startY = start
    finishX, finishY = finish
    return abs(finishX - startX) + abs(finishY - startY)

def read_ride_file(fname):
    file_content = open(fname, 'rb').read().decode('iso-8859-1')
    content = file_content.splitlines()
    first_line = content[0].split(" ")

    rows = int(first_line[0])
    columns = int(first_line[1])
    number_cars = int(first_line[2])
    number_rides = int(first_line[3])
    bonus = int(first_line[4])
    time = int(first_line[5])

    car_list = []
    ride_list = []
    for i in range(number_rides):
        index = i + 1
        ride = content[index].split(" ")
        startX = int(ride[0])
        startY = int(ride[1])
        endX = int(ride[2])
        endY = int(ride[3])
        early_start = int(ride[4])
        late_finish = int(ride[5])
        ride_list += [cTrip(i, (startX, startY), (endX, endY), early_start, late_finish)]

    for i in range(number_cars):
        car_list += [cCar()]

    return rows, columns, bonus, time, ride_list, car_list

def write_file(fname, list_cars):
    with open(fname, 'w') as f:
        for car in list_cars:
            f.write(len(car.completed_trips))
            for trip in car.completed_trips:
                f.write(" " + str(trip.id))
            f.write("\n")
