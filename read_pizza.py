import numpy as np

def read_pizza_file(fname):
    file_content = open(fname, 'rb').read().decode('iso-8859-1')
    content = file_content.splitlines()
    
    first_line = content[0].split(" ")
    rows = int(first_line[0])
    col = int(first_line[1])
    min_ingr = int(first_line[2])
    max_cell = int(first_line[3])
    
    del content[0]
    res=[]
    for line in content:
        res+= line.split()
    res= np.array(res)
    
    return rows, col, min_ingr, max_cell, res


