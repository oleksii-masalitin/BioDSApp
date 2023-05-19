import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def mult(m1, m2):
    m_mult = np.matmul(m1, m2)
    res = np.amax(m_mult, axis=0)
    return res

p = np.array([[1, 9], [0, 1]])
q = np.array([[1, 2], [3, 9]])
print('Result: ', mult(p, q))