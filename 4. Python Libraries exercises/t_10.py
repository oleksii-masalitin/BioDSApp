import numpy as np
import matplotlib.pyplot as plt

def markov_chain(n_states, n_steps, tolerance):
    np.random.seed(1234)
    P = np.random.rand(n_states, n_states)
    p = np.random.rand(n_states)
    for row in P:
        row /= sum(row)
    p /= sum(p)
    for i in range(60):
        p = np.matmul(P.T, p)
    eigvals, eigvectors = np.linalg.eig(P.T)
    for i in range(len(eigvals)):
        if np.abs(eigvals[i] - 1) < 10 ** (-10):
            p_stationary = eigvectors[:, i]
    p_stationary /= sum(p_stationary)
    return p_stationary, p

n_states = 6
n_steps = 60
tolerance = 1e-5
p_stationary, p_last = markov_chain(n_states, n_steps, tolerance)
print(p_stationary, p_last)
