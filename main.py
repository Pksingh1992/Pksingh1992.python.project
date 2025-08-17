from solver import solve_optimization_problem, load_parameters

if __name__ == "__main__":
    params = load_parameters("input_params.json")
    solve_optimization_problem(params)

