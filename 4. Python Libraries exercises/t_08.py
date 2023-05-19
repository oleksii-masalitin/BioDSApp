import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def compute_mandelbrot(n_max, threshold, nx, ny):
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)

    c = x[:,np.newaxis] + 1j * y[np.newaxis,:]
    result = np.ones(shape=np.shape(c), dtype='float64')
    z = np.copy(c)
    for i in range(n_max):
        z = z ** 2 + c
        result[np.abs(z) > threshold] = 0.
    return result


mandelbrot_set = compute_mandelbrot(50, 50., 1801, 1201)
plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
print('Shape: ', mandelbrot_set.shape)
plt.show()