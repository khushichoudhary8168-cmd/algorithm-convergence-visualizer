import numpy as np

def secant(f, x0, x1, tol=1e-6, max_iter=50):
    errors = []
    roots = []

    for i in range(max_iter):
        if f(x1) - f(x0) == 0:
            break

        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        roots.append(x2)

        error = abs(f(x2))
        errors.append(error)

        if error < tol:
            break

        x0, x1 = x1, x2

    return roots, errors