import random
import matplotlib.pyplot as plt
import numpy as np

def generate_initial_state(n):
    return [random.randint(0, 1) for _ in range(n)]

def compute_c(z):
    n = len(z)
    return [[0 if i == j else (2 * z[i] - 1) * (2 * z[j] - 1) for j in range(n)] for i in range(n)]

def sum_matrices(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

def compute_weights_and_theta(c_sum):
    n = len(c_sum)
    w = [[8 * c_sum[i][j] for j in range(n)] for i in range(n)]
    theta = [sum(4 * c_sum[i][j] for j in range(n)) for i in range(n)]
    return w, theta

def hopfield_step(x, w, theta):
    n = len(x)
    x_new = x[:]
    for i in range(n):
        u = sum(w[i][j] * x[j] for j in range(n)) - theta[i]
        if u > 0:
            x_new[i] = 1
        elif u < 0:
            x_new[i] = 0
    return x_new

def plot_final_state(x: list[int]) -> None:
    """Rysuje ostatni stan x jako siatkę 5x5.

    Args:
        x (list[int]): Stan x (25 elementów).
    """
    x_matrix = np.array(x).reshape(5, 5)

    plt.figure(figsize=(5, 5))
    plt.title("Final State (x)")
    plt.imshow(x_matrix, cmap="binary", interpolation="nearest")
    plt.colorbar()
    plt.axis("off")

    for i in range(6):  # Linie poziome
        plt.axhline(i - 0.5, color="black", linewidth=0.5)
    for j in range(6):  # Linie pionowe
        plt.axvline(j - 0.5, color="black", linewidth=0.5)

    plt.show()

z = [
    0,0,0,0,0,
    0,1,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0,
    0,0,1,0,0
]
z_prime = [
    0,1,1,1,0,
    0,1,0,1,0,
    0,1,0,1,0,
    0,1,0,1,0,
    0,1,1,1,0
]

c = compute_c(z)
d = compute_c(z_prime)
c_sum = sum_matrices(c, d)
w, theta = compute_weights_and_theta(c_sum)

x = generate_initial_state(25)

for i in range(10):
    print(f"x({i}):", x)
    plot_final_state(x)
    x = hopfield_step(x, w, theta)

