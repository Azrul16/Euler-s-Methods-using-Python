import numpy as np # type: ignore
from euler_method import euler_method
from systems import harmonic_oscillator

def solve_harmonic_oscillator(t0, y0, t_end, h, omega):
    f = lambda t, yv: harmonic_oscillator(t, yv, omega)
    y0 = np.array([y0, 0])
    t_values, y_values = euler_method(f, t0, y0, t_end, h)
    y_values = y_values[:, 0] if y_values.ndim > 1 else y_values
    return t_values, y_values
