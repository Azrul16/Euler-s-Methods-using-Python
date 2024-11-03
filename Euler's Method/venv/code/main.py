import tkinter as tk
from tkinter import simpledialog, messagebox
import population_modeling
import disease_spread
import projectile_motion
import rc_circuit
import chemical_reaction
import stock_price

class NumericalMethodsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numerical Methods Toolkit")
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select a Problem to Solve:", font=('Arial', 14))
        self.label.pack(pady=10)

        self.buttons = [
            ("Population Modeling", population_modeling.solve_population_problem),
            ("Spread of Diseases", disease_spread.solve_disease_problem),
            ("Projectile Motion", projectile_motion.solve_projectile_problem),
            ("RC Circuit", rc_circuit.solve_rc_circuit_problem),
            ("Chemical Reactions", chemical_reaction.solve_chemical_problem),
            ("Stock Price Prediction", stock_price.solve_stock_price_problem),
        ]

        for text, func in self.buttons:
            button = tk.Button(self.root, text=text, command=lambda f=func: self.run_method(f), font=('Arial', 12))
            button.pack(pady=5)

    def run_method(self, method):
        try:
            result = method()
            messagebox.showinfo("Result", f"Solution: {result}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = NumericalMethodsApp(root)
    root.mainloop()
