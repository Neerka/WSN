import random as rd

def df1_x1(x1, x2, x3):
    return 4*x1 - 2*x2 - 2

def df1_x2(x1, x2, x3):
    return 4*x2 - 2*x1 - 2*x3

def df1_x3(x1, x2, x3):
    return x3*2 - 2*x2 

def f1(x1, x2, x3):
    return 2*x1**2 + 2*x2**2 + x3**2 - 2*x1*x2 - 2*x2*x3 - x1*2 + 3

def initialize_x(size): 
    return [0 for i in range(size)]

def insert_x_values(x, v):
    for i in range(len(x)):
        x[i] = v[i]

def insert_random_x(x, N):
    for i in range(len(x)):
        x[i] = rd.random()*2*N - N

def calculate_diff_f1(x, c):
    d = [df1_x1, df1_x2, df1_x3]
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
    x = initialize_x(3)
    insert_random_x(x, 5) if random else insert_x_values(x, [-4, 0, 4])
    xn = calculate_diff_f1(x, 0.01)
    # print([i for i in x])
    # print([i for i in xn])
    while check_for_eps(xn, x, 0.00001):
        x = xn
        xn = calculate_diff_f1(x, 0.01)
    for i in xn:
        print(f"{i}")
    print(f1(*xn))

# print([rd.random() for i in range(5)])
solve()
