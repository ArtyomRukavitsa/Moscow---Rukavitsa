import copy

import pygame


array = input().split(', ')
arr = []

for el in array:

    el = el[1:-1]
    el = el.split(";")
    x, y = round(float(el[0])), round(float(el[1]))
    arr.append([x, y])
print(arr)
new_arr = []
for el in arr:
    new_arr.append([el[0] + 251, el[1] + 251])
print(new_arr)

arr_copy = copy.copy(new_arr)
pygame.init()

size = width, height = 501, 501
screen = pygame.display.set_mode(size)

running = True
screen.fill(pygame.Color('black'))

again_new = []
k = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 4:
            k += 2

            for el in arr_copy:

                x = el[0]
                y = el[1]
                if y > 251:
                    y += k
                else:
                    y -= k
                if x > 251:
                    x += k
                else:
                    x -= k
                again_new.append([int(x), int(y)])
        if again_new:
            pygame.draw.polygon(screen, (255, 255, 255), again_new, 1)
            new_arr = copy.copy(again_new)
            again_new.clear()
        else:
            pygame.draw.polygon(screen, (255, 255, 255), new_arr, 1)

    pygame.display.flip()
pygame.quit()
