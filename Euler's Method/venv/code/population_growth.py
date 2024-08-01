import numpy as np # type: ignore
from euler_method import euler_method
from systems import population_growth

def solve_population_growth(t0, y0, t_end, h):
    f = population_growth
    y0 = np.array([y0])
    t_values, y_values = euler_method(f, t0, y0, t_end, h)
    y_values = y_values[:, 0] if y_values.ndim > 1 else y_values
    return t_values, y_values
