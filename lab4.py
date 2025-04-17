import random as rd
from math import exp

BETA = 3
C = 0.01
X = ((0,0,1),
     (1,0,1),
     (0,1,1),
     (1,1,1))
Z = (0,0,0,1)
EPSILON = 0.000001

def initialize_s(size) -> list[int]: 
    return [0 for i in range(size)]

def insert_s_values(s: list[int], v: list[int]) -> None:
    for i in range(len(s)):
        s[i] = v[i]

def insert_random_s(s: list[int], N: float) -> None:
    for i in range(len(s)):
        s[i] = rd.random()*2*N - N

def activation(x: float) -> float:
    return 1/(1+exp(-BETA*x))

def activation_prim(x: float) -> float:
    return BETA*activation(x)*(1-activation(x))

def check_for_eps(sn: list[float], so: list[float], epsilon: float) -> bool:
    top = 0
    for n,o in zip(sn, so):
        top = abs(n-o) if abs(n-o) > top else top

    return top > epsilon

def y(p: int, s: list) -> float:
    suma = 0
    for i in range(3):
        suma += s[i] * X[p][i]
    return activation(suma)


def E_dev(s: list) -> list:
    result = [0,0,0]
    y_w = [y(p, s) for p in range(4)]
    # print(y_w)
    for i in range(len(s)):
        for p in range(4):
            suma = 0
            for k in range(3):
                suma += s[k]*X[p][k]
            result[i] += ((y_w[p] - Z[p])*activation_prim(suma)*X[p][i])
    return result

def calculate_new_s(s: list) -> list:
    result = s.copy()
    e = E_dev(s)
    # print(e)
    for i in range(len(result)):
        result[i] = s[i] - C*e[i]
    return result

def solve(random=True):
    s = initialize_s(3)
    insert_random_s(s, 5) if random else insert_s_values(s, [2, 2, 3])
    sn = calculate_new_s(s)
    print([i for i in s])
    t = 0
    while check_for_eps(sn, s, EPSILON):
        s = sn
        sn = calculate_new_s(s)
        t += 1
        # print(sn)
    print("---")
    for i in sn:
        print(f"{i}")
    print("---")
    print(t)

solve()



