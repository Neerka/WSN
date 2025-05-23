import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

def sign_activation(x):
    """Funkcja aktywacji: +1 jeśli x >= 0, inaczej -1"""
    return np.where(x >= 0, 1, -1)

# Wektory q (wejścia testowe)
q_vectors = [
    np.array([-1, -1, 1, -1,  0]),
    np.array([ 1,  1, 1,  1,  0]),
    np.array([ 1, -1, -1, -1, 0]),
    np.array([-1,  1, -1,  1, 0])
]

# Wektory k (lewa część iloczynu tensorowego)
k_vectors = [
    np.array([-1, -1, 1, 0, 0]),
    np.array([ 1,  1, 1, 0, 0]),
    np.array([ 1, -1, -1, 0, 0]),
    np.array([-1,  1, -1, 0, 0])
]

# Wektory v (prawa część iloczynu tensorowego)
v_vectors = [
    np.array([-1, -1,  1, -1, -1]),
    np.array([ 1,  1,  1,  1, -1]),
    np.array([ 1, -1, -1, -1,  1]),
    np.array([-1,  1, -1,  1,  1])
]

# Obliczenie macierzy wag W
W = sum(np.outer(v, k) for v, k in zip(v_vectors, k_vectors))

def run_nakano_hopfield(x0, W, steps=10):
    """Symuluje sieć przez podaną liczbę kroków"""
    x = x0.copy()
    history = [x.copy()]
    for _ in range(steps):
        x = sign_activation(W @ x)
        history.append(x.copy())
    return history

def save_frame(x, t, case, frames_dir="frames11"):
    plt.figure(figsize=(5, 1))
    arr = np.array(x).reshape(1, -1)  # 1x5 pasek
    plt.imshow(arr, cmap='gray', vmin=-1, vmax=1, aspect='auto')
    plt.axis('off')
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    fname = f"{frames_dir}/case{case}_frame_{t}.png"
    plt.savefig(fname, bbox_inches='tight', pad_inches=0)
    plt.close()
    return fname

def create_gif(case, num_steps, frames_dir="frames11", gif_name=None):
    if gif_name is None:
        gif_name = f"simulation11_case{case}.gif"
    images = [imageio.imread(f"{frames_dir}/case{case}_frame_{i}.png") for i in range(num_steps + 1)]
    imageio.mimsave(gif_name, images, duration=500)
    print(f"GIF zapisany jako {gif_name}")

# Testujemy dla q1..q4
gif_steps = 5
for i, x0 in enumerate(q_vectors, start=1):
    print(f"\n--- Warunek początkowy q{i} ---")
    traj = run_nakano_hopfield(x0, W, steps=gif_steps)
    for t, x in enumerate(traj):
        print(f"x({t}) = {x}")
        save_frame(x, t, case=i)
    create_gif(i, gif_steps)

# Testujemy też losowy stan początkowy
random_start = np.random.choice([-1, 1], size=5)
print("\n--- Warunek początkowy: losowy ---")
traj = run_nakano_hopfield(random_start, W, steps=gif_steps)
for t, x in enumerate(traj):
    print(f"x({t}) = {x}")
    save_frame(x, t, case="random")
create_gif("random", gif_steps)
