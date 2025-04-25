import numpy as np
import matplotlib.pyplot as plt

THETA = 2.5/9

x = [0,0,1,0,0,
     0,1,0,0,0,
     0,0,1,0,0,
     0,1,0,0,0,
     0,0,1,0,0]

def f(x:int) -> int:
    """funkcja progowa makaron-pizza

    Args:
        x (int): wejście do funkcji progowej

    Returns:
        int: wyjście 0 dla x < 0, w innym wypadku 1
    """
    return 1 if (1/3**2)*x-THETA >= 0 else 0


def pooling(x: list[int]) -> list[int]:
    """pooling

    Args:
        x (list[int]): input (5x5)

    Returns:
        list[int]: pooled mf (5x5)
    """
    barrier = range(5)
    result = [0 for _ in range(25)]
    for i in range(5):
        for j in range(5):
            suma = 0
            for item1 in (-1,0,1):
                for item2 in (-1,0,1):
                    xidx = (item1+i)*5 + (item2+j)
                    suma += x[xidx] if item1+i in barrier and item2+j in barrier else 0
            result[i*5+j] = f(suma)
    
    return result


def plot_input_and_output(x: list[int], y: list[int]) -> None:
    """Rysuje dane wejściowe x i wynik y jako macierze 5x5.

    Args:
        x (list[int]): Dane wejściowe (5x5).
        y (list[int]): Wynik po pooling (5x5).
    """
    x_matrix = np.array(x).reshape(5, 5)
    y_matrix = np.array(y).reshape(5, 5)

    plt.figure(figsize=(10, 5))

    # Rysowanie x
    plt.subplot(1, 2, 1)
    plt.title("Input (x)")
    plt.imshow(x_matrix, cmap="binary", interpolation="nearest")
    plt.colorbar()
    plt.axis("off")

    # Rysowanie y
    plt.subplot(1, 2, 2)
    plt.title("Output (y)")
    plt.imshow(y_matrix, cmap="binary", interpolation="nearest")
    plt.colorbar()
    plt.axis("off")

    plt.tight_layout()
    plt.show()

y = pooling(x)

plot_input_and_output(x, y)