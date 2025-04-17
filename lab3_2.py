import random as rd
import numpy as np
np.random.seed(10)

def df2_x1(x1, x2):
    return 12*x1**3 + 12*x1**2 - 24*x1

def df2_x2(x1, x2):
    return 24*x2 - 24

def f2(x1,x2):
    return 3*x1**4 + 4*x1**3 - 12*x1**2 + 12*x2**2 - 24*x2

def initialize_x(size): 
    return [0 for i in range(size)]

def insert_x_values(x, v):
    for i in range(len(x)):
        x[i] = v[i]

def insert_random_x(x, N):
    for i in range(len(x)):
        x[i] = rd.random()*2*N - N

def calculate_diff_f1(x, c):
    d = [df2_x1, df2_x2]
    result = [xi for xi in x]
    for i in range(len(result)):
        result[i] = x[i] - c*d[i](*x)
    return result

def check_for_eps(xn, xo, epsilon):
    top = 0
    for n,o in zip(xn, xo):
        top = abs(n-o) if abs(n-0) > top else top

    return top > epsilon

def solve(random=True):
    x = initialize_x(2)
    insert_random_x(x, 3) if random else insert_x_values(x, [-4, 4])
    xn = calculate_diff_f1(x, 0.01)
    # print([i for i in x])
    # print([i for i in xn])
    while check_for_eps(xn, x, 0.00001):
        x = xn
        xn = calculate_diff_f1(x, 0.01)
    for i in xn:
        print(f"{i}")
    print(f2(*xn))

# print([rd.random() for i in range(5)])
solve()