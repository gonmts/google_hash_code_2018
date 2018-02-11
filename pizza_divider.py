import numpy as np

def pizza_divider(pizza, x, y):
    number_of_x = pizza.shape[0] // x
    number_of_y = pizza.shape[1] // y
    subpizza = []
    for i in range(number_of_x):
        for k in range(number_of_y):
            j = i*x
            m = k*y
            subpizza += [pizza[j:j+x, m:m+y]]
    return np.array(subpizza)
