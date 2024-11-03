import numpy as np
from tkinter import Toplevel, Label, Entry, Button, StringVar

def solve_projectile_problem():
    def calculate_position():
        v0 = float(entry_v0.get())
        angle = float(entry_angle.get())
        t_end = float(entry_t_end.get())
        h = float(entry_h.get())

        g = 9.81

        angle_rad = np.radians(angle)
        vx = v0 * np.cos(angle_rad)
        vy = v0 * np.sin(angle_rad)

        def fx(t, vx):
            return 0

        def fy(t, vy):
            return -g

        t = np.arange(0, t_end + h, h)
        x = np.zeros(t.shape)
        y = np.zeros(t.shape)
        y[0] = 0

        for i in range(1, t.size):
            vx += h * fx(t[i-1], vx)
            vy += h * fy(t[i-1], vy)
            x[i] = x[i-1] + h * vx
            y[i] = y[i-1] + h * vy
        
        result.set(f"Position after {t_end} seconds: ({x[-1]}, {y[-1]})")

    window = Toplevel()
    window.title("Projectile Motion")

    Label(window, text="Initial Velocity (m/s):").grid(row=0, column=0)
    entry_v0 = Entry(window)
    entry_v0.grid(row=0, column=1)

    Label(window, text="Angle of Projection (degrees):").grid(row=1, column=0)
    entry_angle = Entry(window)
    entry_angle.grid(row=1, column=1)

    Label(window, text="Time Period (seconds):").grid(row=2, column=0)
    entry_t_end = Entry(window)
    entry_t_end.grid(row=2, column=1)

    Label(window, text="Step Size (seconds):").grid(row=3, column=0)
    entry_h = Entry(window)
    entry_h.grid(row=3, column=1)

    result = StringVar()
    Label(window, textvariable=result).grid(row=5, columnspan=2, pady=10)

    Button(window, text="Calculate", command=calculate_position).grid(row=4, columnspan=2, pady=10)
