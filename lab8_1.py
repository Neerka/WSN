import numpy as np
import matplotlib.pyplot as plt

THETA = 2.5

u1 = [0,0,0,0,0,
      0,1,1,1,0,
      0,1,0,1,0,
      0,1,1,1,0,
      0,0,0,0,0]

u2 = [0,0,0,0,0,
      0,0,0,0,0,
      1,1,1,0,0,
      1,0,1,0,0,
      1,1,1,0,0]

u3 = [0,0,0,0,0,
      1,1,0,0,0,
      0,1,0,0,0,
      0,1,0,0,0,
      0,1,0,0,0]

w = [1,1,1,
     1,0,0,
     1,0,0]

def f(x:int) -> int:
    """funkcja progowa makaron-pizza

    Args:
        x (int): wejście do funkcji progowej

    Returns:
        int: wyjście 0 dla x < 0, w innym wypadku 1
    """
    return 1 if x-THETA >= 0 else 0

def convolution(bitmap: list[int], kernel: list[int]) -> list[int]:
    """Convoluts the input with use of kernel.

    Args:
        bitmap (list[int]): a bitmap to be convoluted (must be length 25)
        kernel (list[int]): kernel used to convolut (must be length 9)

    Returns:
        list[int]: convoluted image
    """
    barrier = range(5)
    result = [0 for _ in range(25)]
    for i in range(5):
        for j in range(5):
            suma = 0
            for item1 in (-1,0,1):
                for item2 in (-1,0,1):
                    bidx = (i+item1)*5+(j+item2)
                    kidx = 3*(item1+1)+(item2+1) 
                    suma += bitmap[bidx]*kernel[kidx] if i+item1 in barrier and j+item2 in barrier else 0
            result[i*5+j] = f(suma)

    return result

def plot_results(inputs, results, titles):
    """Plots the input bitmaps and their corresponding results.

    Args:
        inputs (list[list[int]]): List of input bitmaps (each of length 25).
        results (list[list[int]]): List of result bitmaps (each of length 25).
        titles (list[str]): Titles for the plots.
    """
    fig, axes = plt.subplots(2, len(inputs), figsize=(12, 6))
    for idx, (input_bitmap, result_bitmap) in enumerate(zip(inputs, results)):
        # Plot input bitmap
        axes[0, idx].imshow(np.array(input_bitmap).reshape(5, 5), cmap='binary', vmin=0, vmax=1)
        axes[0, idx].set_title(f"{titles[idx]} Input")
        axes[0, idx].axis('off')

        # Plot result bitmap
        axes[1, idx].imshow(np.array(result_bitmap).reshape(5, 5), cmap='binary', vmin=0, vmax=1)
        axes[1, idx].set_title(f"{titles[idx]} Result")
        axes[1, idx].axis('off')

    plt.tight_layout()
    plt.show()

x1, x2, x3 = convolution(u1, w), convolution(u2, w), convolution(u3, w)

# Prepare data for plotting
inputs = [u1, u2, u3]
results = [x1, x2, x3]
titles = ["u1", "u2", "u3"]

# Plot the inputs and results
plot_results(inputs, results, titles)