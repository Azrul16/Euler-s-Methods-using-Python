import numpy as np
from tkinter import Toplevel, Label, Entry, Button, StringVar

def solve_rc_circuit_problem():
    def calculate_voltage():
        R = float(entry_R.get())
        C = float(entry_C.get())
        V0 = float(entry_V0.get())
        t_end = float(entry_t_end.get())
        h = float(entry_h.get())

        def voltage_drop(t, V):
            return -V / (R * C)

        t = np.arange(0, t_end + h, h)
        V = np.zeros(t.shape)
        V[0] = V0
        for i in range(1, t.size):
            V[i] = V[i-1] + h * voltage_drop(t[i-1], V[i-1])
        
        result.set(f"Voltage after {t_end} seconds: {V[-1]} V")

    window = Toplevel()
    window.title("RC Circuit")

    Label(window, text="Resistance (ohms):").grid(row=0, column=0)
    entry_R = Entry(window)
    entry_R.grid(row=0, column=1)

    Label(window, text="Capacitance (farads):").grid(row=1, column=0)
    entry_C = Entry(window)
    entry_C.grid(row=1, column=1)

    Label(window, text="Initial Voltage (V):").grid(row=2, column=0)
    entry_V0 = Entry(window)
    entry_V0.grid(row=2, column=1)

    Label(window, text="Time Period (seconds):").grid(row=3, column=0)
    entry_t_end = Entry(window)
    entry_t_end.grid(row=3, column=1)

    Label(window, text="Step Size (seconds):").grid(row=4, column=0)
    entry_h = Entry(window)
    entry_h.grid(row=4, column=1)

    result = StringVar()
    Label(window, textvariable=result).grid(row=6, columnspan=2, pady=10)

    Button(window, text="Calculate", command=calculate_voltage).grid(row=5, columnspan=2, pady=10)
