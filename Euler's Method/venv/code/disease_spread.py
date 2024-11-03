import numpy as np
from tkinter import Toplevel, Label, Entry, Button, StringVar

def solve_disease_problem():
    def calculate_infected():
        I0 = float(entry_I0.get())
        k = float(entry_k.get())
        t_end = float(entry_t_end.get())
        h = float(entry_h.get())

        def infection_rate(t, I):
            return k * I

        t = np.arange(0, t_end + h, h)
        I = np.zeros(t.shape)
        I[0] = I0
        for i in range(1, t.size):
            I[i] = I[i-1] + h * infection_rate(t[i-1], I[i-1])
        
        result.set(f"Number of infected people after {t_end} days: {I[-1]}")

    window = Toplevel()
    window.title("Spread of Diseases")

    Label(window, text="Initial Infected People:").grid(row=0, column=0)
    entry_I0 = Entry(window)
    entry_I0.grid(row=0, column=1)

    Label(window, text="Infection Rate:").grid(row=1, column=0)
    entry_k = Entry(window)
    entry_k.grid(row=1, column=1)

    Label(window, text="Time Period (days):").grid(row=2, column=0)
    entry_t_end = Entry(window)
    entry_t_end.grid(row=2, column=1)

    Label(window, text="Step Size (days):").grid(row=3, column=0)
    entry_h = Entry(window)
    entry_h.grid(row=3, column=1)

    result = StringVar()
    Label(window, textvariable=result).grid(row=5, columnspan=2, pady=10)

    Button(window, text="Calculate", command=calculate_infected).grid(row=4, columnspan=2, pady=10)
