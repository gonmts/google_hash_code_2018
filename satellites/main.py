from read_file import *
from cImage import *
from cSatellite import *
from calc_score import *
from tqdm import tqdm

def main():
    filename_input = ""
    number_turns, sat_list, collection, photo_list = read_file(filename_input)

    sat_dict = {}
    for i in range(len(sat_list)):
        my_id = sat_list[i].id
        positions = sat_list[i].initList(number_turns)
        for k in range(len(positions)):
            pos = positions[k]
            sat_dict[my_id] = list_photos_in_range(sat_list[i], pos, photo_list, k)

    for t in tqdm(range(number_turns)):
        for sat_id in sat_dict.keys():
            photo_in_frame = sat_dict[sat_id][t]
            index_of_pic_taken = -1
            for q in range(len(photo_in_frame)):
                photo = photo_in_frame[q]
                if sat_list[sat_id].isInRange(photo[1]):
                    sat_list[sat_id].track(photo[1])
                    for p in range(1, len(photo)):
                        photo[p].instagram(t, sat_id)
                    index_of_pic_taken = q
                    break
            if index_of_pic_taken >= 0:
                del photo_in_frame[index_of_pic_taken]
            sat_dict[sat_id].updatePosition(t)
