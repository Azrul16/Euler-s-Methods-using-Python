import numpy as np
from tkinter import Toplevel, Label, Entry, Button, StringVar

def solve_population_problem():
    def calculate_population():
        P0 = float(entry_P0.get())
        r = float(entry_r.get())
        t_end = float(entry_t_end.get())
        h = float(entry_h.get())

        def population_growth(t, P):
            return r * P

        t = np.arange(0, t_end + h, h)
        P = np.zeros(t.shape)
        P[0] = P0
        for i in range(1, t.size):
            P[i] = P[i-1] + h * population_growth(t[i-1], P[i-1])
        
        result.set(f"Population after {t_end} months: {P[-1]}")

    window = Toplevel()
    window.title("Population Modeling")

    Label(window, text="Initial Population:").grid(row=0, column=0)
    entry_P0 = Entry(window)
    entry_P0.grid(row=0, column=1)

    Label(window, text="Growth Rate (as a decimal):").grid(row=1, column=0)
    entry_r = Entry(window)
    entry_r.grid(row=1, column=1)

    Label(window, text="Time Period (months):").grid(row=2, column=0)
    entry_t_end = Entry(window)
    entry_t_end.grid(row=2, column=1)

    Label(window, text="Step Size (months):").grid(row=3, column=0)
    entry_h = Entry(window)
    entry_h.grid(row=3, column=1)

    result = StringVar()
    Label(window, textvariable=result).grid(row=5, columnspan=2, pady=10)

    Button(window, text="Calculate", command=calculate_population).grid(row=4, columnspan=2, pady=10)
