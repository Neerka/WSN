import random

def generate_initial_state(n):
    return [random.randint(0, 1) for _ in range(n)]

def compute_c(z):
    n = len(z)
    c = [[0 if i == j else (2 * z[i] - 1) * (2 * z[j] - 1) for j in range(n)] for i in range(n)]
    return c

def compute_weights_and_theta(c):
    n = len(c)
    w = [[8 * c[i][j] for j in range(n)] for i in range(n)]
    theta = [sum(4 * c[i][j] for j in range(n)) for i in range(n)]
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
        # else: x[i] stays the same
    return x_new

# Przykład użycia:
z = [1] * 25  # lub jakiś inny wzorzec
c = compute_c(z)
w, theta = compute_weights_and_theta(c)
x = generate_initial_state(25)

print("x(0):", x)
x = hopfield_step(x, w, theta)
print("x(1):", x)
x = hopfield_step(x, w, theta)
print("x(2):", x)
