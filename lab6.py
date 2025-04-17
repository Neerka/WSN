import numpy as np
import os
import tensorflow as tf
import random as rd
np.random.seed(10)

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

N = 3
C = 0.01
MOMENTUM = 0.0  # 0.0 do zadania 1., inne do zadania 2.

def init():
    X = tf.Variable(np.random.uniform(-N, N), trainable=False)
    Y = tf.Variable(np.random.uniform(-N, N), trainable=False)
    return X, Y

def f(x1,x2):
    return 3*x1**4 + 4*x1**3 - 12*x1**2 + 12*x2**2 - 24*x2

X, Y = init()
minimum = f(X.numpy(), Y.numpy())

for _ in range(5):
    opt = tf.compat.v1.train.MomentumOptimizer(learning_rate=C, momentum=MOMENTUM)
    for epoch in range(1000):
        opt.minimize(lambda: f(X,Y), var_list=[X,Y])
        print((f(X,Y)).numpy(), X.numpy(), Y.numpy(), end="\r")
    print(X.numpy(), Y.numpy(), f(X,Y).numpy())
    X, Y = init()