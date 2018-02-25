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
