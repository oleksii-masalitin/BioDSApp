import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def solve_system(a, b):
    a = np.array(a)
    b = np.array(b)
    sol = np.linalg.solve(a, b)
    return sol

print('Result: ', solve_system([[3,1], [1,2]], [9,8]))

