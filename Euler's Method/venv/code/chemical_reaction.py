import numpy as np
from tkinter import Toplevel, Label, Entry, Button, StringVar

def solve_chemical_problem():
    def calculate_concentration():
        C0 = float(entry_C0.get())
        k = float(entry_k.get())
        t_end = float(entry_t_end.get())
        h = float(entry_h.get())

        def concentration_change(t, C):
            return -k * C

        t = np.arange(0, t_end + h, h)
        C = np.zeros(t.shape)
        C[0] = C0
        for i in range(1, t.size):
            C[i] = C[i-1] + h * concentration_change(t[i-1], C[i-1])
        
        result.set(f"Concentration after {t_end} seconds: {C[-1]} M")

    window = Toplevel()
    window.title("Chemical Reactions")

    Label(window, text="Initial Concentration (M):").grid(row=0, column=0)
    entry_C0 = Entry(window)
    entry_C0.grid(row=0, column=1)

    Label(window, text="Rate Constant (s^-1):").grid(row=1, column=0)
    entry_k = Entry(window)
    entry_k.grid(row=1, column=1)

    Label(window, text="Time Period (seconds):").grid(row=2, column=0)
    entry_t_end = Entry(window)
    entry_t_end.grid(row=2, column=1)

    Label(window, text="Step Size (seconds):").grid(row=3, column=0)
    entry_h = Entry(window)
    entry_h.grid(row=3, column=1)

    result = StringVar()
    Label(window, textvariable=result).grid(row=5, columnspan=2, pady=10)

    Button(window, text="Calculate", command=calculate_concentration).grid(row=4, columnspan=2, pady=10)
