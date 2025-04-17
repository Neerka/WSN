# MODEL M-P

def check(*x: int):
    if x not in {0,1}:
        raise ValueError
    return True

def f(x: float) -> int:
    return 0 if x < 0 else 1

def dot(w: list, u: list) -> float:
    result = 0
    if len(w) != len(u):
        raise IndexError
    for i in range(len(w)):
        result += w[i]*u[i]
    return result

def NOT(u1: int) -> int:
    w = [-2, 1] # Przykładowe wartości - w1 < w2  oraz w2 >= 0
    u = [u1, 1]
    try:
        check(*u)

        iloczyn = dot(w,u)
        return f(iloczyn)
    except:
        print(f'Niepoprawna wartość u1')

def AND(u1: int, u2: int) -> int:
    w = [2,2,-3] # Przykładowe wartości - -w3 =< w1 + w2 < -2*w3 oraz w3 < 0
    u = [u1, u2, 1]
    try:
        check(*u)

        iloczyn = dot(w,u)
        return f(iloczyn)
    except:
        print(f'Niepoprawne wartości u1 lub u2')

def NAND(u1: int, u2: int) -> int:
    w = [-2, -2, 3.5] # Przykładowe wartości - -2*w3 =< w1 + w2 < -w3 oraz w3 >= 0
    u = [u1, u2, 1]
    try:
        check(*u)

        iloczyn = dot(w,u)
        return f(iloczyn)
    except:
        print(f'Niepoprawne wartości u1 lub u2')

def OR(u1: int, u2: int) -> int:
    w = [1 , 1, -1] # Przykładowe wartości - w1 + w2 >= -2*w3 oraz w3 < 0
    u = [u1, u2, 1]
    try:
        check(*u)

        iloczyn = dot(w,u)
        return f(iloczyn)
    except:
        print(f'Niepoprawne wartości u1 lub u2')

def inputLoop():
    while True:
        print(f"Co chcesz policzyć?\n1. NOT\n2. AND\n3. NAND\n4. OR\nWpisz 5 żeby wyjść")
        choice = input()
        if choice == "1":
            u1 = int(input("Podaj wartość u1: "))
            print(f"Oto twój wynik:\n{NOT(u1)}\n")
        elif choice == "5":
            break
        else:
            u1 = int(input("Podaj wartość u1: "))
            u2 = int(input("Podaj wartość u2: "))
            if choice == "2":
                print(f"Oto twój wynik:\n{AND(u1, u2)}\n")
            elif choice == "3":
                print(f"Oto twój wynik:\n{NAND(u1, u2)}\n")
            elif choice == "4":
                print(f"Oto twój wynik:\n{OR(u1, u2)}\n")

inputLoop()