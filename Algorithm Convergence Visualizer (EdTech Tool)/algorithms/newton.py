import numpy as np

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def newton(f, x0, tol=1e-6, max_iter=50):
    errors = []
    roots = []

    x = x0

    for i in range(max_iter):
        roots.append(x)
        error = abs(f(x))
        errors.append(error)

        if error < tol:
            break

        d = derivative(f, x)
        if d == 0:
            break

        x = x - f(x) / d

    return roots, errors