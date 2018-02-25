def calc_score(collection):
    score = 0
    for key in collection.keys():
        all_taken = True
        for photo in collection[key]:
            all_taken = all_taken and photo.done
            if not all_taken:
                break
        if all_taken:
            score += (collection[key][0] * len(collection[key]))
    return score

def is_in_time(photo_turn, conditions):
    for cond in conditions:
        if photo_turn >= cond[0] and photo_turn <= cond[1]:
            return True
    return False

def list_photos_in_range(satellite, position, list_photos, time):
    photos_dict = {}
    for photo in list_photos:
        if satellite.isInWishfulRange(position, photo) and is_in_time(time, photo.time):
            if photo.pos not in photos_dict:
                photos_dict[photo.pos] = [0]
            photos_dict[photo.pos][0] += photo.score
            photos_dict[photo.pos] += [photo]

    return sorted(photos_dict.values(), key=lambda x: x[0])
