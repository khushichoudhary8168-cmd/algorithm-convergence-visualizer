# Algorithm Convergence Visualizer & Numerical Methods Toolkit

A modular and interactive application built using Streamlit to visualize, compare, and analyze numerical methods for solving nonlinear equations and ordinary differential equations.

---

## Overview

This project is designed as a comprehensive toolkit for studying numerical methods. It provides both:

* Root-finding algorithms for nonlinear equations
* Numerical solvers for differential equations

The application emphasizes convergence analysis, error tracking, and method comparison through real-time visualizations and structured outputs.

---

## Key Features

### Root-Finding Algorithms

* Bisection Method
* Newton-Raphson Method
* Secant Method

### Differential Equation Solvers

* Euler Method
* Adams-Bashforth Method (4th order)
* Finite Difference Method
* Milne Predictor-Corrector Method

### Visualization & Analysis

* Iteration-wise error tracking
* Real-time convergence animation
* Comparative plots (multi-method)
* Tabular representation of results
* Export functionality (CSV and graphs)

---

## Project Architecture

The project follows a modular structure with separate implementations for each algorithm:

```bash
.
├── app.py                  # Streamlit UI and visualization logic
├── algorithms/
│   ├── bisection.py       # Bisection method implementation
│   ├── newton.py          # Newton-Raphson method
│   ├── secant.py          # Secant method
│   └── differential.py    # ODE solvers (Euler, Adams, Milne, etc.)
├── requirements.txt
└── README.md
```

---

## Implementation Details

### Root Finding

Each method computes iterative approximations and tracks error reduction per iteration. These values are used to analyze convergence speed and stability.

### Differential Methods

The ODE solvers are implemented using standard numerical techniques:

* Euler method for basic approximation
* Adams-Bashforth for higher-order prediction
* Milne method using predictor-corrector approach
* Finite difference for discrete approximation

Example (Euler method implementation):

```python
def euler_method(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        xs.append(x0)
        ys.append(y0)

    return xs, ys
```

---

## Installation and Usage

```bash
git clone https://github.com/your-username/algorithm-convergence-visualizer.git
cd algorithm-convergence-visualizer
pip install -r requirements.txt
streamlit run app.py
```

---

## Application Workflow

1. Enter a function ( f(x) ) or differential equation ( dy/dx = f(x, y) )
2. Select one or more numerical methods
3. Configure parameters (initial values, tolerance, iterations, step size)
4. Run the simulation
5. Analyze results through graphs, tables, and animations

---

## Results

The application provides:

* Convergence graphs comparing multiple methods
* Iteration-wise error tables
* Numerical solution plots for differential equations
* Downloadable outputs for further analysis

---

## Key Learnings

* Comparison of convergence rates (linear, quadratic, superlinear)
* Trade-offs between accuracy and computational cost
* Practical implementation of classical numerical methods
* Visualization of iterative algorithms

---

## Future Enhancements

* Support for symbolic differentiation
* Additional numerical methods (Runge-Kutta, etc.)
* Improved UI with advanced plotting libraries
* Web deployment for public access

---

## Author

Khushi Choudhary
Computer Science Engineering Student
Aspiring Data Analyst

---

## License

This project is intended for educational and learning purposes.
