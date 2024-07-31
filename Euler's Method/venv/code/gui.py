import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt # type: ignore
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # type: ignore

from euler_method import euler_method
from systems import example_function, harmonic_oscillator, population_growth # type: ignore

class EulerSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Euler's Method Solver")
        
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.system_var = tk.StringVar(value="Example Function")
        self.systems = ["Example Function", "Harmonic Oscillator", "Population Growth"]
        self.create_widgets()

    def create_widgets(self):
        system_label = ttk.Label(self.frame, text="Select System:")
        system_label.grid(row=0, column=0, padx=5, pady=5)
        system_menu = ttk.OptionMenu(self.frame, self.system_var, self.systems[0], *self.systems)
        system_menu.grid(row=0, column=1, padx=5, pady=5)

        t0_label = ttk.Label(self.frame, text="Initial Time (t0):")
        t0_label.grid(row=1, column=0, padx=5, pady=5)
        self.t0_entry = ttk.Entry(self.frame)
        self.t0_entry.grid(row=1, column=1, padx=5, pady=5)

        y0_label = ttk.Label(self.frame, text="Initial Value (y0):")
        y0_label.grid(row=2, column=0, padx=5, pady=5)
        self.y0_entry = ttk.Entry(self.frame)
        self.y0_entry.grid(row=2, column=1, padx=5, pady=5)

        t_end_label = ttk.Label(self.frame, text="End Time:")
        t_end_label.grid(row=3, column=0, padx=5, pady=5)
        self.t_end_entry = ttk.Entry(self.frame)
        self.t_end_entry.grid(row=3, column=1, padx=5, pady=5)

        h_label = ttk.Label(self.frame, text="Step Size (h):")
        h_label.grid(row=4, column=0, padx=5, pady=5)
        self.h_entry = ttk.Entry(self.frame)
        self.h_entry.grid(row=4, column=1, padx=5, pady=5)

        omega_label = ttk.Label(self.frame, text="Omega (for Harmonic Oscillator):")
        omega_label.grid(row=5, column=0, padx=5, pady=5)
        self.omega_entry = ttk.Entry(self.frame)
        self.omega_entry.grid(row=5, column=1, padx=5, pady=5)

        solve_button = ttk.Button(self.frame, text="Solve and Plot", command=self.solve_and_plot)
        solve_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def solve_and_plot(self):
        system = self.system_var.get()
        t0 = float(self.t0_entry.get())
        y0 = float(self.y0_entry.get())
        t_end = float(self.t_end_entry.get())
        h = float(self.h_entry.get())

        if system == "Example Function":
            f = example_function
            y0 = np.array([y0])
        elif system == "Harmonic Oscillator":
            omega = float(self.omega_entry.get())
            f = lambda t, yv: harmonic_oscillator(t, yv, omega)
            y0 = np.array([y0, 0])
        elif system == "Population Growth":
            f = population_growth
            y0 = np.array([y0])
        
        t_values, y_values = euler_method(f, t0, y0, t_end, h)
        y_values = y_values[:, 0] if y_values.ndim > 1 else y_values

        fig, ax = plt.subplots()
        ax.plot(t_values, y_values, label=system)
        ax.set_xlabel('Time (t)')
        ax.set_ylabel('y(t)')
        ax.set_title('Euler Method Approximation')
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def main():
    root = tk.Tk()
    app = EulerSolverGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
