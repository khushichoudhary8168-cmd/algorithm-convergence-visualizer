import numpy as np

def bisection(f, a, b, tol=1e-6, max_iter=50):
    errors = []
    roots = []

    for i in range(max_iter):
        c = (a + b) / 2
        roots.append(c)
        error = abs(f(c))
        errors.append(error)

        if error < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return roots, errors