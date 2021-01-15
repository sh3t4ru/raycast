from rayengine import *
import time
import pygame

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

    s1 = Sphere(Coordinate(100.0, 100.0, 50.0), "#aa50bb", 40.0)
    s2 = Sphere(Coordinate(140.0, 140.0, 40.0), "#ffa500", 40.0)
    s3 = Sphere(Coordinate(100.0, 70.0, 40.0), "#20b2aa", 20.0)
    s4 = Sphere(Coordinate(120.0, 100.0, 38.0), "#696969", 29.0)

    start_time = time.time()
    cr = 0.0
    cst = 0.0
    drw = 0.0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            start_time = time.time()
            for i in range(2):
                ray = Ray(Coordinate(100.0, 100.0, -800.0), Coordinate(x - 100.0, y - 100.0, 800.0))
            cr += time.time() - start_time

            start_time = time.time()
            color = cast_ray(ray, [s1, s2, s3, s4])
            cst += time.time() - start_time
            #        color = cast_ray(ray, [s1])
            start_time = time.time()
            screen.set_at((x, y), color)
            drw += time.time() - start_time

    print(cr, cst, drw)
    pygame.display.flip()

pygame.quit()
