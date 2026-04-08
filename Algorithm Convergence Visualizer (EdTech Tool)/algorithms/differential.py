import numpy as np

# ---------------- EULER METHOD ----------------
def euler_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h

        xs.append(x0)
        ys.append(y0)

    return xs, ys

# ---------------- FINITE DIFFERENCE ----------------
def finite_difference(f, x0, y0, h, n):
    xs = np.linspace(x0, x0 + n*h, n+1)
    ys = np.zeros(n+1)

    ys[0] = y0

    for i in range(n):
        ys[i+1] = ys[i] + h * f(xs[i], ys[i])  # forward diff approx

    return xs, ys


# ---------------- ADAMS-BASHFORTH 4 ----------------
def adams_bashforth_4(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    # Use Euler to generate first 4 values
    for i in range(3):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        xs.append(x0)
        ys.append(y0)

    for i in range(3, n):
        y_next = ys[i] + (h/24) * (
            55*f(xs[i], ys[i])
            - 59*f(xs[i-1], ys[i-1])
            + 37*f(xs[i-2], ys[i-2])
            - 9*f(xs[i-3], ys[i-3])
        )

        x_next = xs[i] + h

        xs.append(x_next)
        ys.append(y_next)

    return xs, ys


# ---------------- MILNE METHOD ----------------
def milne_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    # Step 1: Generate first 4 points using Euler
    for i in range(3):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        xs.append(x0)
        ys.append(y0)

    # Step 2: Milne Predictor-Corrector
    for i in range(3, n):
        # Predictor
        y_pred = ys[i-2] + (4*h/3) * (
            2*f(xs[i], ys[i])
            - f(xs[i-1], ys[i-1])
            + 2*f(xs[i-2], ys[i-2])
        )

        x_next = xs[i] + h

        # Corrector
        y_corr = ys[i-1] + (h/3) * (
            f(x_next, y_pred)
            + 4*f(xs[i], ys[i])
            + f(xs[i-1], ys[i-1])
        )

        xs.append(x_next)
        ys.append(y_corr)

    return xs, ys




