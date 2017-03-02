import pygame
from pygame.locals import *
import sys

M = 'M'
T = 'T'
E = '0'
row = 0
col = 0
min = 0
max = 0
pizza = None
nbM = 0
nbT = 0

def search_pizza(i, j, min, max, pizza):
    size_pizza_T = 0
    size_pizza_M = 0


    coord_i = i
    coord_j = j

    while size_pizza_M < max and size_pizza_T < max:
        check = False
        if coord_i + 1 < len(pizza[j]):
            add_T = 0
            add_M = 0
            for x in range(j, coord_j + 1):
                if pizza[x][coord_i + 1] == T:
                    add_T += 1
                elif pizza[x][coord_i + 1] == M:
                    add_M += 1

            if add_T + size_pizza_T <= max or add_M + size_pizza_M <= max:
                coord_i += 1
                size_pizza_T += add_T
                size_pizza_M += add_M
                check = True

        if coord_j + 1 < len(pizza):
            add_T = 0
            add_M = 0
            for x in range(i, coord_i + 1):
                if pizza[coord_j + 1][x] == T:
                    add_T += 1
                elif pizza[coord_j + 1][x] == M:
                    add_M += 1

            if add_T + size_pizza_T <= max or add_M + size_pizza_M <= max:
                check = True
                coord_j += 1
                size_pizza_T += add_T
                size_pizza_M += add_M
        if not check:
            break

    if coord_j == j and coord_i == i:
        return None
    return (coord_i, coord_j)



def algo():
    global nbM
    global nbT

    for line in pizza:
        nbM += line.count(M)
        nbT += line.count(T)

    i = 0
    j = 0
    max_line = len(pizza[0])
    res = []
    while j < len(pizza):
        while i < max_line and pizza[j][i] == E:
            i += 1
        if i == max_line:
            i = 0
            j += 1
            continue

        coord_pizza = search_pizza(i, j, min, max, pizza)

        if coord_pizza == None:
            m = list(pizza[j])
            m[i] = E
            pizza[j] = m
            continue

        res.append([i, j, coord_pizza[0], coord_pizza[1]])
        for x in range(j, coord_pizza[1] + 1):
            for y in range(i, coord_pizza[0] + 1):
                m = list(pizza[x])
                m[y] = E
                pizza[x] = m
        j += 1

    for line in res:
        print(str(line[0]) + " " + str(line[1]) + " " + str(line[2]) + " " + str(line[3]))

    return res

def random_color():
    import random
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)

def draw_res(res):
    pygame.init()

    DISPLAY = pygame.display.set_mode((500, 500), 0, 32)

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    blue = (0, 0, 255)

    DISPLAY.fill(BLACK)
    i = 0
    for line in res:
        c = random_color()
        while c == (0, 0, 0):
            c = random_color()
        pygame.draw.rect(DISPLAY, c, (line[0]  * (500 / col) , line[1] * (500 / row), (line[2] + 1) * (500 / col), (line[3] + 1) * (500 / row)))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    file = open("small.in")
    content = file.read()
    content = content.split('\n')
    row = int(content[0].split(' ')[0])
    col = int(content[0].split(' ')[1])
    min = int(content[0].split(' ')[2])
    max = int(content[0].split(' ')[3])
    pizza = content[1:]
    pizza = pizza[:-1]
    res = algo()
    draw_res(res)
