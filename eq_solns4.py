def find_solutions(n, C, current_solution=[], results=[]):
    if n == 1:
        # We are at the last variable, it must be whatever remains of C
        current_solution.append(C)
        results.append(current_solution.copy())
        current_solution.pop()  
    else:
        # Try all possible values for the current variable
        for i in range(C + 1):
            current_solution.append(i)
            find_solutions(n - 1, C - i, current_solution, results)
            current_solution.pop()  

    return results

def print_solutions(n, C):
    results = find_solutions(n, C)
    for solution in results:
        print(solution)


n = int(input("enter the number of terms: "))
c = int(input("enter the constant term: "))

print_solutions(n, c)
