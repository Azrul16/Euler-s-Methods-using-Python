import numpy as np

def example_function(t, y):
    return -2 * t * y

def harmonic_oscillator(t, yv, omega):
    y, v = yv
    dydt = v
    dvdt = -omega**2 * y
    return np.array([dydt, dvdt])

def population_growth(t, y):
    r = 0.1
    return r * y
