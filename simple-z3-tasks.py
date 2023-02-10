from z3 import *


def is_prime(n):
    solver = Solver()
    x = Int("x")
    solver.add(x > 1, x < n, n % x == 0)

    if solver.check() == sat:
        return False
    else:
        return True


def independent_set(list_of_edges, num_nodes):
    solver = Solver()
    nodes = [Bool("v%d" % i) for i in range(num_nodes)]
    for i, j in list_of_edges:
        solver.add(Or(Not(nodes[i]), Not(nodes[j])))

    if solver.check() == sat:
        # Get the optimal solution
        model = solver.model()
        # Print the vertices that are in the independent set
        print("Vertices in the maximum independent set:", [i for i in range(num_nodes) if is_true(model[nodes[i]])])
    else:
        print("No solution found.")


print(is_prime(25))  # False
print(is_prime(13))  # True
edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6)]
independent_set(edges, 7)
