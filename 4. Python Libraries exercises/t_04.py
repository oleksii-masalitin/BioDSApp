import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def add_mean_and_calc_det(matrix):
    matrix = matrix.astype('float64')
    size = np.shape(matrix)[0]
    for i in range(size):
        mean = np.mean(matrix[i, :])
        matrix[i, :] += mean
    return np.linalg.det(matrix)


print('Result:', add_mean_and_calc_det(np.array([[5, 3, 4], [7, 9, 8], [6, 7, 8]])))
