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
    nodes = [Int("v%d" % i) for i in range(num_nodes)]
    for i, j in list_of_edges:
        solver.add(Or(Not(nodes[i] == 1), Not(nodes[j] == 1)))

    for i in range(num_nodes):
        solver.add(Or(nodes[i] == 1, nodes[i] == 0))

    model = solver.model
    for s in range(num_nodes):
        solver.add(sum(nodes) > s)
        if solver.check() == sat:
            model = solver.model()

        else:
            break
            #  print("None")
    print("Maximum independent set:", [i for i in range(num_nodes) if (model[nodes[i]]) == 1])


print(is_prime(25))  # False
print(is_prime(13))  # True
edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6)]
independent_set(edges, 7)  # [0, 3, 5, 6]
