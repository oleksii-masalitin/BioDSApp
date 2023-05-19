import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def nearest_to_scalar(matrix, n):
    new_matrix = abs(matrix - n)
    closest_value_index = np.unravel_index(new_matrix.argmin(), new_matrix.shape)
    return matrix[closest_value_index]

print('Nearest:', nearest_to_scalar(np.array([[5, 3, 4], [7, 9, 8], [6, 7, 8]]), 11))