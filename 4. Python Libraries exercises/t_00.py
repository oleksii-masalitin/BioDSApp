import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def checkerboard(n, m):
    chessboard = np.zeros(shape=(n, m), dtype='int32')
    for i in range(n):
        for j in range(m):
            chessboard[i, j] = (i + j) % 2
    return chessboard

print('Checkerboard pattern: \n', checkerboard(4, 3))