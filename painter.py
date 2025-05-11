from rayengine import *
import pygame

WIDTH = 320
HEIGHT = 240
FPS = 60

RAYCAST_WIDTH = 160
RAYCAST_HEIGHT = 120
SCALE_FACTOR = WIDTH // RAYCAST_WIDTH

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ray Casting Demo - Drag spheres with mouse, scroll to change depth")
clock = pygame.time.Clock()

render_surface = pygame.Surface((RAYCAST_WIDTH, RAYCAST_HEIGHT))

spheres = [
    Sphere((100.0, 100.0, 50.0), "#aa50bb", 40.0),  # Purple
    Sphere((140.0, 140.0, 40.0), "#ffa500", 40.0),  # Orange
    Sphere((100.0, 70.0, 40.0), "#20b2aa", 20.0),   # Light sea green
    Sphere((120.0, 100.0, 38.0), "#696969", 29.0)   # Dark gray
]

selected_sphere = None
last_mouse_pos = None
camera_pos = (100.0, 100.0, -800.0)
Z_DEPTH_STEP = 5.0
needs_update = True

def get_ray_from_mouse(mouse_pos):
    x, y = mouse_pos
    x = x // SCALE_FACTOR
    y = y // SCALE_FACTOR
    return Ray(camera_pos, (x - RAYCAST_WIDTH//2, y - RAYCAST_HEIGHT//2, 800.0))

def find_closest_sphere(mouse_pos):
    ray = get_ray_from_mouse(mouse_pos)
    closest_sphere = None
    min_distance = float('inf')
    
    for sphere in spheres:
        impact, distance = sphere.intersect(ray)
        if impact and distance < min_distance:
            min_distance = distance
            closest_sphere = sphere
    
    return closest_sphere

def move_sphere(sphere, mouse_pos):
    ray = get_ray_from_mouse(mouse_pos)
    t = (sphere.center[2] - camera_pos[2]) / ray.vector[2]
    new_x = camera_pos[0] + ray.vector[0] * t
    new_y = camera_pos[1] + ray.vector[1] * t
    sphere.center = (new_x, new_y, sphere.center[2])
    global needs_update
    needs_update = True

def change_sphere_depth(sphere, delta):
    x, y, z = sphere.center
    new_z = z + delta
    new_z = max(20.0, min(100.0, new_z))
    sphere.center = (x, y, new_z)
    global needs_update
    needs_update = True

def render_scene():
    for x in range(RAYCAST_WIDTH):
        for y in range(RAYCAST_HEIGHT):
            ray = Ray(camera_pos, (x - RAYCAST_WIDTH//2, y - RAYCAST_HEIGHT//2, 800.0))
            color = cast_ray(ray, spheres)
            r, g, b = map(lambda x: int(x, 16), (color[1: 3], color[3: 5], color[5: 7]))
            render_surface.set_at((x, y), (r, g, b))

running = True
while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                selected_sphere = find_closest_sphere(event.pos)
                last_mouse_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                selected_sphere = None
                last_mouse_pos = None
        elif event.type == pygame.MOUSEMOTION:
            if selected_sphere and last_mouse_pos:
                move_sphere(selected_sphere, event.pos)
                last_mouse_pos = event.pos
        elif event.type == pygame.MOUSEWHEEL:
            if selected_sphere:
                change_sphere_depth(selected_sphere, event.y * Z_DEPTH_STEP)

    if needs_update:
        render_scene()
        needs_update = False

    screen.fill((0, 0, 0))
    
    scaled_surface = pygame.transform.scale(render_surface, (WIDTH, HEIGHT))
    screen.blit(scaled_surface, (0, 0))

    pygame.display.flip()

pygame.quit()
