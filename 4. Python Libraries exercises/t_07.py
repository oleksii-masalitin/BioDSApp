import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def complex_sort(complex_nums):
    return sorted(complex_nums, key=lambda num: (np.real(num), np.imag(num)))

print('Result: ', complex_sort([1 + 2j, 3 - 1j, 3 - 2j, 4 - 3j, 3 + 5j]))