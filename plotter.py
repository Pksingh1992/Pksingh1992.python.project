# plotter.py
import numpy as np
import matplotlib.pyplot as plt

def plot_optimization_solution(x_opt, y_opt):
    # Define range for x1 and x2
    x = np.linspace(0, 60, 400)
    y = np.linspace(0, 60, 400)

    # Constraints (material, labor, machine time)
    c1 = (100 - 2 * x)          # 2*x + y <= 100 → y <= 100 - 2x
    c2 = (80 - x)               # x + y <= 80 → y <= 80 - x
    c3 = (90 - x) / 3           # x + 3y <= 90 → y <= (90 - x)/3

    plt.figure(figsize=(8, 6))
    plt.plot(x, c1, label=r'$2x + y \leq 100$')
    plt.plot(x, c2, label=r'$x + y \leq 80$')
    plt.plot(x, c3, label=r'$x + 3y \leq 90$')

    # Fill feasible region
    y_max = np.minimum(np.minimum(c1, c2), c3)
    plt.fill_between(x, 0, y_max, color='lightgrey', alpha=0.5)

    # Plot optimal solution point
    plt.plot(x_opt, y_opt, 'ro', label='Optimal Solution')

    plt.xlim((0, 60))
    plt.ylim((0, 60))
    plt.xlabel('Product A units (x1)')
    plt.ylabel('Product B units (x2)')
    plt.title('Feasible Region and Optimal Solution')
    plt.legend()
    plt.grid(True)
    plt.show()

