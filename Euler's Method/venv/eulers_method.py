import math
import matplotlib.pyplot as plt # type: ignore

def ac_circuit_cli():
  """
  Command-line interface for AC circuit calculations with visualization.
  """

  try:
    resistance = float(input("Enter resistance (ohms): "))
    capacitance = float(input("Enter capacitance (farads): "))
    frequency = float(input("Enter frequency (Hz): "))

    omega = 2 * math.pi * frequency
    capacitive_reactance = 1 / (omega * capacitance)
    impedance = complex(resistance, -capacitive_reactance)

    print("Impedance:", impedance)
    print("Magnitude:", abs(impedance), "ohms")
    print("Phase angle:", math.degrees(math.atan2(impedance.imag, impedance.real)), "degrees")

    # Visualization
    plt.figure(figsize=(5, 5))
    plt.plot(impedance.real, impedance.imag, 'ro')
    plt.grid(True)
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.title('Impedance Plot')
    plt.show()

  except ValueError:
    print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
  ac_circuit_cli()
