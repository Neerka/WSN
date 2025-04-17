import random as rd
import numpy as np
import matplotlib.pyplot as plt

BETA = 1
c = 0.8
EPSILON = 0.0001

np.random.seed(42)

u1 = [1,1,0,0,1,0,0,1,0,1]
u2 = [0,0,1,0,0,1,0,0,1,1]
w1 = [20,0,0,0,0,0,0,0,0,-10]
w2 = [0,0,20,0,0,0,0,0,0,-10]
s = [[20*u1[_],20*u2[_],-10] for _ in range(9)]

def f(x:float)-> float:
    return 1/(1+np.exp(-BETA*x))

def f_prim(x:float) -> float:
    return BETA*f(x)*(1-f(x))

def x(u: list[float], w: list[float]) -> float:
    suma = 0
    for i in range(10):
        suma += w[i]*u[i]
    return f(suma)

def encoder(u: list[float]) -> list[float]:
    x_vec = [0 for _ in range(3)]
    x_vec[0] = x(u,w1)
    x_vec[1] = x(u,w2)
    x_vec[2] = 1.0
    return x_vec

def decoder(x_vec: list[float]) -> list[float]:
    y_vec = [0 for _ in range(9)]
    for j in range(9):
        suma = 0
        for i in range(3):
            suma += s[i][j] * x_vec[i]
        y_vec[j] = f(suma)
    return y_vec

def calculate_s(y1,y2, u1,u2, x1,x2):
    for i in range(3):
        for j in range(9):
            z1 = (y1[j] - u1[j])*f_prim(np.dot(s[j], x1))*x1[i]
            z2 = (y2[j] - u2[j])*f_prim(np.dot(s[j], x2))*x2[i]
            z = z1+z2
            s[i][j] = s[i][j] - z  # TODO Naprawić

def E(y1, y2, u1, u2):
    suma = 0
    for t in range(9):
        suma += (y1[t] - u1[t])**2 + (y2[t] - u2[t])**2
    return suma/2

def plot_grid(data, title):
    """
    Wyświetla dane jako obrazek w siatce 3x3.
    :param data: Lista 9 wartości do wyświetlenia.
    :param title: Tytuł obrazka.
    """
    grid = np.array(data[:9]).reshape(3, 3)  # Przekształcenie na siatkę 3x3
    plt.imshow(grid, cmap='gray', interpolation='nearest')
    plt.title(title)
    plt.colorbar()
    plt.xticks([])
    plt.yticks([])

def plot_vector(data, title):
    """
    Wyświetla dane jako obrazek w siatce 3x1.
    :param data: Lista 3 wartości do wyświetlenia.
    :param title: Tytuł obrazka.
    """
    grid = np.array(data[:3]).reshape(1, 3)  # Przekształcenie na siatkę 1x3
    plt.imshow(grid, cmap='gray', interpolation='nearest', aspect='auto')
    plt.title(title)
    plt.colorbar()
    plt.xticks(range(3))
    plt.yticks([])

if __name__=="__main__":
    x1, x2 = encoder(u1), encoder(u2)
    y1, y2 = decoder(x1), decoder(x2)

    # Tworzenie wykresów
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plot_grid(u1, "Input u1")

    plt.subplot(2, 2, 2)
    plot_grid(u2, "Input u2")

    plt.subplot(2, 2, 3)
    plot_grid(y1, "Output y1")

    plt.subplot(2, 2, 4)
    plot_grid(y2, "Output y2")

    plt.tight_layout()
    plt.show()
