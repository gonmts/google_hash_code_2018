from cSatellite import cSatellite
from cImage import cImage
import numpy as np

def read_file(fname):
    sat_list = []
    photo_list = []
    collection = {}

    file_content = open(fname, 'rb').read().decode('iso-8859-1')
    content = file_content.splitlines()

    number_turns = int(content[0])
    number_sat = int(content[1])
    index = 2
    for i in range(number_sat):
        line = content[2 + i].split(" ")
        lat = int(line[0])
        log = int(line[1])
        vel = int(line[2])
        max_change = int(line[3])
        max_value = int(line[4])

        sat_list += [cSatellite(i, lat, log, vel, max_change, max_value)]
        index += 1

    number_collection = int(content[index])
    index += 1
    while index < len(content):
        first_line = content[index].split(" ")
        value = int(first_line[0])
        number_locs = int(first_line[1])
        number_times = int(first_line[2])
        index += 1
        list_loc = []
        list_time = []
        col = []

        for loc in range(number_locs):
            l = content[index].split(" ")
            list_loc += [[int(l[0]), int(l[1])]]
            index += 1
        for t in range(number_times):
            start, end = content[index].split(" ")
            list_time += [[int(start), int(end)]]
            index += 1
        for image in list_loc:
            image = [cImage(image, list_time, value / number_locs)]
            photo_list += image
            col += image
        collection[index] = col

    return number_turns, sat_list, collection, photo_list

def write_file(fname, collections):
    lst_taken = []
    for key in collections.keys():
        lst = collections[key]
        for photo in lst:
            if photo.done:
                lst_taken += [photo]

    with open(fname, 'w') as f:
        f.write('{}\n'.format(len(lst_taken)))
        for photo in lst_taken:
            f.write(str(photo.pos[0]) + " " + str(photo.pos[1]) + " " + str(photo.sat_done) + " " + str(photo.time_done) + "\n")
