from algorithms.bisection import bisection
from algorithms.newton import newton
from algorithms.secant import secant
from utils.plotter import plot_convergence

# Define function
def f(x):
    return x**3 - x - 2

# Run algorithms
_, errors_b = bisection(f, 1, 2)
_, errors_n = newton(f, 1.5)
_, errors_s = secant(f, 1, 2)

# Store results
results = {
    "Bisection": errors_b,
    "Newton": errors_n,
    "Secant": errors_s
}

# Plot
plot_convergence(results)