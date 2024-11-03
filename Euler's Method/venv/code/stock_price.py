import numpy as np

def solve_stock_price_problem():
    P0 = float(input("Enter initial stock price ($): "))
    r = float(input("Enter growth rate (as a decimal): "))
    t_end = float(input("Enter the time period (months): "))
    h = float(input("Enter the step size (months): "))

    def price_change(t, P):
        return r * P

    t = np.arange(0, t_end + h, h)
    P = np.zeros(t.shape)
    P[0] = P0
    for i in range(1, t.size):
        P[i] = P[i-1] + h * price_change(t[i-1], P[i-1])
    
    return f"Stock price after {t_end} months: ${P[-1]:.2f}"
