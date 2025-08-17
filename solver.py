import json
from scipy.optimize import linprog
from plotter import plot_optimization_solution

def load_parameters(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def solve_optimization_problem(params):
    profit = params["profit"]
    constraints = params["constraints"]
    bounds_raw = params["bounds"]

    # linprog minimizes, so negate profits for maximization
    c = [-p for p in profit]

    A = constraints["A"]
    b = constraints["b"]

    # Convert JSON null to Python None for bounds
    bounds = [(b[0], b[1]) for b in bounds_raw]

    result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

    if result.success:
        x_opt = result.x
        print("✅ Optimal solution found:")
        for i, x in enumerate(x_opt):
            print(f" - Variable x{i+1}: {x:.2f}")
        print(f" - Maximum profit: ${-result.fun:.2f}")

        if len(x_opt) == 2:
            plot_optimization_solution(x_opt[0], x_opt[1])
    else:
        print("❌ Optimization failed:", result.message)


