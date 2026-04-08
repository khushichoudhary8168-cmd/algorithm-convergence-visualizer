import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
from io import BytesIO

from algorithms.bisection import bisection
from algorithms.newton import newton
from algorithms.secant import secant
from algorithms.differential import (
    euler_method, adams_bashforth_4, finite_difference, milne_method
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Algorithm Visualizer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Algorithm Convergence Visualizer")
st.markdown("### 🚀 Real-Time Comparison of Numerical Methods")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")

# Root Finding
func_input = st.sidebar.text_input("Enter function f(x):", "x**3 - x - 2")

methods = st.sidebar.multiselect(
    "Select Root Methods",
    ["Bisection", "Newton", "Secant"],
    default=["Bisection", "Newton", "Secant"]
)

tol = st.sidebar.slider("Tolerance", 1e-6, 1e-2, 1e-4, format="%.6f")
max_iter = st.sidebar.slider("Max Iterations", 10, 100, 50)

# Differential
st.sidebar.markdown("### 📘 Differential Equation")

diff_eq = st.sidebar.text_input("dy/dx = f(x,y):", "x + y")
x0 = st.sidebar.number_input("Initial x0", value=0.0)
y0 = st.sidebar.number_input("Initial y0", value=1.0)
h = st.sidebar.number_input("Step size (h)", value=0.1)
n = st.sidebar.slider("Steps", 5, 50, 20)

diff_methods = st.sidebar.multiselect(
    "Select Differential Methods",
    ["Euler", "Adams-Bashforth 4", "Finite Difference", "Milne"],
    default=["Euler"]
)

# ---------------- FUNCTIONS ----------------
def f(x):
    try:
        return eval(func_input, {"x": x, "np": np})
    except:
        return np.nan

def f_diff(x, y):
    try:
        return eval(diff_eq, {"x": x, "y": y, "np": np})
    except:
        return 0

# ---------------- FUNCTION GRAPH ----------------
st.subheader("📘 Function Graph")

x_vals = np.linspace(-5, 5, 200)
y_vals = [f(x) for x in x_vals]

fig_func, ax_func = plt.subplots()
ax_func.plot(x_vals, y_vals)
ax_func.axhline(0)
ax_func.set_title("Function")
ax_func.grid()

st.pyplot(fig_func)

# ---------------- ROOT VISUALIZATION ----------------
if st.button("▶️ Run Root Visualization"):

    results = {}

    if "Bisection" in methods:
        _, errors_b = bisection(f, 1, 2, tol, max_iter)
        results["Bisection"] = errors_b

    if "Newton" in methods:
        _, errors_n = newton(f, 1.5, tol, max_iter)
        results["Newton"] = errors_n

    if "Secant" in methods:
        _, errors_s = secant(f, 1, 2, tol, max_iter)
        results["Secant"] = errors_s

    if not results:
        st.warning("⚠️ Select at least one method")
    else:
        # -------- Animation --------
        st.subheader("📈 Live Convergence")
        placeholder = st.empty()
        fig, ax = plt.subplots()

        max_len = max(len(v) for v in results.values())

        for i in range(max_len):
            ax.clear()

            for name, errors in results.items():
                upto = min(i + 1, len(errors))
                ax.plot(errors[:upto], label=name, marker='o')

            ax.set_xlabel("Iterations")
            ax.set_ylabel("Error")
            ax.set_title("Convergence (Live)")
            ax.legend()
            ax.grid()

            placeholder.pyplot(fig)
            time.sleep(0.2)

        # -------- Final Graph --------
        st.subheader("📊 Final Comparison Graph")
        fig_final, ax_final = plt.subplots()

        for name, errors in results.items():
            ax_final.plot(errors, label=name, marker='o')

        ax_final.set_xlabel("Iterations")
        ax_final.set_ylabel("Error")
        ax_final.legend()
        ax_final.grid()

        st.pyplot(fig_final)

        # -------- Table --------
        table_data = {}

        for name, errors in results.items():
            table_data[name] = errors

        max_len = max(len(v) for v in table_data.values())

        for key in table_data:
            table_data[key] += [None] * (max_len - len(table_data[key]))

        df = pd.DataFrame(table_data)

        st.subheader("📋 Convergence Table")
        st.dataframe(df)

        # -------- Download Table --------
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Table", csv, "root_results.csv", "text/csv")

        # -------- Download Graph --------
        buf = BytesIO()
        fig_final.savefig(buf, format="png")
        buf.seek(0)

        st.download_button("⬇️ Download Graph", buf, "root_graph.png", "image/png")

# ---------------- DIFFERENTIAL SECTION ----------------
st.subheader("📊 Differential Equation Solution")

if st.button("▶️ Solve Differential Equation"):

    fig_diff, ax_diff = plt.subplots()
    table_data = {}

    if "Euler" in diff_methods:
        xs, ys = euler_method(f_diff, x0, y0, h, n)
        ax_diff.plot(xs, ys, label="Euler", marker='o')
        table_data["x"] = xs
        table_data["Euler"] = ys

    if "Adams-Bashforth 4" in diff_methods:
        xs, ys = adams_bashforth_4(f_diff, x0, y0, h, n)
        ax_diff.plot(xs, ys, label="Adams-Bashforth", marker='o')
        table_data["Adams-Bashforth"] = ys

    if "Finite Difference" in diff_methods:
        xs, ys = finite_difference(f_diff, x0, y0, h, n)
        ax_diff.plot(xs, ys, label="Finite Difference", marker='o')
        table_data["Finite Difference"] = ys

    if "Milne" in diff_methods:
        xs, ys = milne_method(f_diff, x0, y0, h, n)
        ax_diff.plot(xs, ys, label="Milne", marker='o')
        table_data["Milne"] = ys

    if not table_data:
        st.warning("⚠️ Select at least one method")
    else:
        ax_diff.set_xlabel("x")
        ax_diff.set_ylabel("y")
        ax_diff.set_title("Differential Equation Solutions")
        ax_diff.legend()
        ax_diff.grid()

        st.pyplot(fig_diff)

        # -------- Table --------
        df = pd.DataFrame(table_data)

        st.subheader("📋 Differential Table")
        st.dataframe(df)

        # -------- Download Table --------
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Table", csv, "diff_results.csv", "text/csv")

        # -------- Download Graph --------
        buf = BytesIO()
        fig_diff.savefig(buf, format="png")
        buf.seek(0)

        st.download_button("⬇️ Download Graph", buf, "diff_graph.png", "image/png")

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("👩‍💻 Built by Khushi & Preeti")


##cd "C:\Users\HP\Desktop\26iot\Project\Algorithm Convergence Visualizer (EdTech Tool)"  streamlit run app.py
