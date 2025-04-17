import random as rd
from math import exp

BETA = 1
C = 0.1
U = ((0,0,1),
     (1,0,1),
     (0,1,1),
     (1,1,1))
Z = (0,1,1,0)
EPSILON = 0.0001

def initialize_s(size) -> list[int]: 
    return [0 for i in range(size)]

def insert_s_values(s: list[int], v: list[int]) -> None:
    for i in range(len(s)):
        s[i] = v[i]

def insert_random_s(s: list[int], N: float) -> None:
    for i in range(len(s)):
        s[i] = rd.random()*2*N - N

def initialize_w(size) -> list[int]: 
    return [[0 for j in range(size)] for i in range(size-1)]

def insert_w_values(w: list[int], v: list[int]) -> None:
    for i in range(len(w)):
        for j in range(len(w[i])):
            w[i][j] = v[len(w[i])*i+j]

def insert_random_w(w: list[int], N: float) -> None:
    for i in range(len(w)):
        for j in range(len(w[i])):
            w[i][j] = rd.random()*2*N - N

def activation(x: float) -> float:
    return 1/(1+exp(-BETA*x))

def activation_prim(x: float) -> float:
    return BETA*activation(x)*(1-activation(x))

def check_for_eps(sn: list[float], so: list[float], wn: list[list[float]], wo: list[list[float]], epsilon: float) -> bool:
    top_s = 0
    top_w = 0
    for n,o in zip(sn, so):
        top_s = abs(n-o) if abs(n-o) > top_s else top_s
    
    for i in range(len(wn)):
        for j in range(len(wn[i])):
            top_w = abs(wn[i][j] - wo[i][j]) if abs(wn[i][j] - wo[i][j]) > top_w else top_w

    top = max(top_w, top_s)
    return top > epsilon

def y(p: int, s: list) -> float:
    suma = 0
    for i in range(3):
        suma += s[i] * U[p][i]
    return activation(suma)

