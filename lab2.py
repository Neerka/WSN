import numpy as np
import pygame as pg

u1: list[int] = [-1, -1, -1, -1, -1,
                 -1,  1,  1,  1, -1,
                 -1,  1,  -1,  1, -1,
                 -1,  1,  1,  1, -1,
                 -1, -1, -1, -1, -1]

u2: list[int] = [-1, -1, -1, -1, -1,
                 -1,  1,  1, -1, -1,
                 -1, -1,  1, -1, -1,
                 -1, -1,  1, -1, -1,
                 -1, -1, -1, -1, -1]

u1prim: list[int] = [-1,  1,  1,  1, -1,
                  -1,  1, -1,  1, -1,
                  -1,  1, -1,  1, -1,
                  -1,  1,  1,  1, -1,
                  -1, -1, -1, -1, -1]

u2prim: list[int] = [-1, -1,  1, -1, -1,
                  -1, -1,  1, -1, -1,
                  -1, -1,  1, -1, -1,
                  -1, -1,  1, -1, -1,
                  -1, -1, -1, -1, -1]

def wyswietl(u: list[int]) -> None:
    print("-"*7)
    for i in range(0, 25, 5):
        napis = "|"
        for j in range(5):
            if u[i + j] == 1:
                napis += "X"
            else:
                napis += " "
        napis += "|"
        print(napis)
    print("-"*7)


def policzW() -> np.ndarray:
    global u1, u2
    u1 = np.array(u1)
    u2 = np.array(u2)
    W = np.zeros((25, 25))
    for i in range(25):
        for j in range(25):
            W[i][j] = (u1[i] * u1[j])/25  + (u2[i] * u2[j])/25
    return W


def fi(u: list[int]) -> list[int]:
    W = policzW()
    u = np.array(u)
    y = np.zeros(25)
    for i in range(25):
        suma = 0
        for j in range(25):
            suma += W[i][j] * u[j]
        y[i] = 1 if suma >= 0 else -1
    return y

print("Wynik dla u1:")
wyswietl(fi(u1))
print()
print("Wynik dla u2:")
wyswietl(fi(u2))
print()
print("Wynik dla u1':")
wyswietl(fi(u1prim))
print()
print("Wynik dla u2':")
wyswietl(fi(u2prim))
# print(policzW())

def draw_grid(screen, u, offset_x, offset_y):
    for i in range(5):
        for j in range(5):
            color = (0, 0, 0) if u[i * 5 + j] == 1 else (255, 255, 255)
            pg.draw.rect(screen, color, pg.Rect(j * 50 + offset_x, i * 50 + offset_y, 50, 50))
            pg.draw.rect(screen, (0, 0, 0), pg.Rect(j * 50 + offset_x, i * 50 + offset_y, 50, 50), 1)

def draw_text(screen, text, x, y):
    font = pg.font.Font(None, 36)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (x, y))

def main():
    pg.init()
    screen = pg.display.set_mode((550, 600))
    pg.display.set_caption("Wyniki")
    
    u1_result = fi(u1)
    u2_result = fi(u2)
    u1p_result = fi(u1prim)
    u2p_result = fi(u2prim)
    
    screen.fill((255, 255, 255))
    draw_grid(screen, u1_result, 0, 0)
    draw_text(screen, "u1", 100, 260)
    draw_grid(screen, u2_result, 300, 0)
    draw_text(screen, "u2", 400, 260)
    draw_grid(screen, u1p_result, 0, 300)
    draw_text(screen, "u1p", 100, 560)
    draw_grid(screen, u2p_result, 300, 300)
    draw_text(screen, "u2p", 400, 560)
    pg.display.flip()
    
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    pg.quit()

if __name__ == "__main__":
    main()