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


pygame.init()

size = width, height = 501, 501
screen = pygame.display.set_mode(size)

running = True


again_new = []
k = 1
while running:
    screen.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 4:
            k += 2
    print(k)
    for el in arr:
        x = el[0]
        y = el[1]
        if y > 0:
            y += k
        else:
            y -= k
        if x > 0:
            x += k
        else:
            x -= k
        again_new.append([int(x) + 251, int(y) + 251])
    pygame.draw.polygon(screen, (255, 255, 255), again_new, 1)
    again_new.clear()
    pygame.display.flip()
pygame.quit()