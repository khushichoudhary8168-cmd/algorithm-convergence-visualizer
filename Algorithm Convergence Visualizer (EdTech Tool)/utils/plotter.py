import matplotlib.pyplot as plt

def plot_convergence(results):
    for name, errors in results.items():
        plt.plot(errors, label=name)

    plt.xlabel("Iterations")
    plt.ylabel("Error")
    plt.title("Algorithm Convergence Comparison")
    plt.legend()
    plt.grid()

    plt.show()