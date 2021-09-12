import pygame
import sys
import pyautogui

#Make a variable so that u dont have to add one for each while true loop

width, height = 600,450
win = (width, height)
screen = pygame.display.set_mode(win)
xaxis = width/1.80 + 150
yaxis = height/2
scale = 200
iterations = 35 # the more iterations you make the better resolustion you'll get
zoom = 30

#Screenshots
frame = 1
counter = 0
a = 15

mouse_list = []

def take_screen_shot():
    global frame
    save_file = "screenshots/"+ str(frame) + ".png"
    pygame.image.save(screen, save_file)
    print("A screen shot has been saved as: " + save_file)

frames = 6000
for i in range(frames): #frames
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
            if event.key == pygame.MOUSEBUTTONDOWN:
                mouse_list.clear()
                mouse_list.append(pygame.mouse.get_pos())

    counter += 1
    scale += zoom
    zoom += 5
    if counter >= 25:
        zoom += 30
    elif counter >= 100:
        zoom *= zoom
    elif counter == a:
        a+=a
        iterations += a/3

    for iy in range(int(height / 2 + 1)):
        for ix in range(width):
            z = 0 + 0j
            c = complex(float(ix - xaxis) / scale-1.6, float(iy - yaxis) / scale)
            x = c.real
            y = c.imag
            y2 = y * y
            q = (x - 0.25) ** 2 + y2
            if not (q * (q + (x - 0.25)) < y2 / 4.0 or (x + 1.0) ** 2 + y2 < 0.0625):
                for i in range(iterations):
                    z = z ** 2 + c # ** = times itself x times
                    if abs(z) > 2:
                        v = 765 * i / iterations
                        if v > 510:
                            color = (255, 255, v % 255)
                        elif v > 255:
                            color = (100, v % 255, 255)
                        else:
                            color = (0, 0, v % 255)
                        break
                    else:
                        color = (0, 0, 0)

            screen.set_at((ix, iy), color)
            screen.set_at((ix, height - iy), color)

    pygame.display.update()
    take_screen_shot()
    frame += 1

pygame.quit()
