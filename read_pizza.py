import numpy as np

def read_pizza_file(filename):
    with open(fname) as f:
        content = f.readlines()
        first_line = content[0].split(" ")
        rows = int(first_line[0])
        col = int(first_line[1])
        min_ingr = int(first_line[2])
        max_cell = int(first_line[3])

        res = []
        for line in content[1,:]:
            l = []
            for letter in line:
                l += [letter]
            res += [l]
        res = np.array(res)

        return {"rows": rows, "col": col, "L": min_ingr, "H": max_cell, "pizza": res}
