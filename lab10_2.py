import numpy as np
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os

def generate_initial_state(n):
    return np.random.randint(0, 2, size=n)

def compute_c(z):
    n = len(z)
    c = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                c[i][j] = (2 * z[i] - 1) * (2 * z[j] - 1)
    return c

def sum_matrices(a, b):
    n = len(a)
    return a + b

def compute_weights_and_theta(c_sum):
    w = 8 * c_sum
    theta = 4 * np.sum(c_sum, axis=1)
    return w, theta

def sigmoid(u, T):
    return 1 / (1 + np.exp(-u / T))

def hopfield_step_sigmoid(x, w, theta, T):
    n = len(x)
    new_x = np.zeros(n, dtype=int)
    for i in range(n):
        u_i = np.dot(w[i], x) - theta[i]
        beta_i = np.random.uniform(0, 1)
        if beta_i <= sigmoid(u_i, T):
            new_x[i] = 1
        else:
            new_x[i] = 0
    return new_x

def save_frame(x, t, frames_dir="frames"):
    arr = np.array(x).reshape(5, 5)
    plt.imshow(arr, cmap='gray', vmin=0, vmax=1)
    plt.axis('off')
    if not os.path.exists(frames_dir):
        os.makedirs(frames_dir)
    fname = f"{frames_dir}/frame_{t}.png"
    plt.savefig(fname, bbox_inches='tight', pad_inches=0)
    plt.close()
    return fname

def create_gif(num_steps, frames_dir="frames", gif_name="simulation10_2.gif"):
    images = [imageio.imread(f"{frames_dir}/frame_{i}.png") for i in range(num_steps + 1)]
    imageio.mimsave(gif_name, images, duration=500)
    print(f"GIF zapisany jako {gif_name}")

def main():
    n = 25
    T = 25
    num_steps = 25
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
    c_sum = c + d  # numpy arrays, so this is element-wise sum
    w, theta = compute_weights_and_theta(c_sum)
    x = generate_initial_state(n)
    print("x(0):", x)
    frames_dir = "frames"
    save_frame(x, 0, frames_dir)
    for t in range(1, num_steps + 1):
        x = hopfield_step_sigmoid(x, w, theta, T)
        print(f"x({t}):", x)
        save_frame(x, t, frames_dir)
    create_gif(num_steps, frames_dir, "simulation10_2.gif")

if __name__ == "__main__":
    main()
