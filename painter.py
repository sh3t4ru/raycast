from rayengine import *
import time
import pygame
from pygame import gfxdraw

WIDTH = 320
HEIGHT = 240
FPS = 10


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    s1 = Sphere((100.0, 100.0, 50.0), "#aa50bb", 40.0)
    # s2 = Sphere((140.0, 140.0, 40.0), "#ffa500", 40.0)
    # s3 = Sphere((100.0, 70.0, 40.0), "#20b2aa", 20.0)
    # s4 = Sphere((120.0, 100.0, 38.0), "#696969", 29.0)


    cr = 0.0
    cst = 0.0
    drw = 0.0
    start_time = time.time()
#    pixel_array = pygame.PixelArray(screen)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            start_time = time.time()
            ray = Ray((100.0, 100.0, -800.0), (x - 100.0, y - 100.0, 800.0))
            cr += time.time() - start_time

            start_time = time.time()
#            color = cast_ray(ray, [s1, s2, s3, s4])
            color = cast_ray(ray, [s1])
            cst += time.time() - start_time

            r, g, b = map(lambda x: int(x, 16), (color[1: 3], color[3: 5], color[5: 7]))
            start_time = time.time()
#            screen.set_at((x, y), color)
            gfxdraw.pixel(screen, x, y, (r, g, b))
#            pixel_array[x, y] = (r, g, b)
            drw += time.time() - start_time

    print(cr, cst, drw)
    pygame.display.flip()

pygame.quit()
