def find_solutions(n, C, current_solution=[], results=[]):
    if n == 1:
        # We are at the last variable, it must be whatever remains of C
        current_solution.append(C)
        results.append(current_solution.copy())
        current_solution.pop()  # Remove last element to explore other possibilities
    else:
        # Try all possible values for the current variable
        for i in range(C + 1):
            current_solution.append(i)
            find_solutions(n - 1, C - i, current_solution, results)
            current_solution.pop()  # Remove last element to explore other possibilities

    return results

def print_solutions(n, C):
    results = find_solutions(n, C)
    for solution in results:
        print(" + ".join(map(str, solution)), "=", C)

# Example usage:
n = 3  # number of variables
C = 4  # constant sum
print_solutions(n, C)
