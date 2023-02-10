from z3 import *


def is_prime(n):
    solver = Solver()
    x = Int("x")
    solver.add(x > 1, x < n, n % x == 0)

    if solver.check() == sat:
        return False
    else:
        return True


def find_path(graph):
    n = len(graph)  # number of nodes
    solver = Solver()
    nodes = [Bool(f"node_{i}") for i in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                solver.add(Implies(nodes[i], nodes[j]))  # adding edges


print(is_prime(25))  # False
print(is_prime(13))  # True
