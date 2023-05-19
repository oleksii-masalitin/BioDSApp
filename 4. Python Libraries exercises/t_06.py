import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def svd_ranks(Z):
     U, S, V = np.linalg.svd(Z)
     return np.linalg.matrix_rank(U), np.linalg.matrix_rank(np.diag(S)), np.linalg.matrix_rank(V)

print('Svd ranks:', svd_ranks(np.arange(9).reshape((3, 3))))
