import pygame
import random

#   setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

pygame.display.set_caption("snake")

#   game properties
width = screen.get_width()
height = screen.get_height()
cube_size = 30
player_size = 40
player_pos = pygame.Vector2(width / 4, height / 2)
movement_speed = 200

#   cube list, event and functions
cubes = []

SPAWN_CUBE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_CUBE_EVENT, 5000) # 10 sec

def getPosCube():
    # positions with safezones
    x = random.randint(cube_size, width - cube_size)
    y = random.randint(cube_size, height - cube_size)

    pos = pygame.Vector2(x, y)
    return pos

def spawnCube():
    cube_pos = getPosCube()
    cubes.append(cube_pos)



while running:
    #   delta time (60fps)
    dt = clock.tick(60) / 1000

    #   close game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_CUBE_EVENT:
            print("cube spawned")
            spawnCube()
            
    #   render player
    screen.fill ("green")
    pygame.draw.rect(screen, "red", pygame.Rect(player_pos.x, player_pos.y, player_size, player_size))

    #   render cubes
    for cube_pos in cubes:
        if cube_pos is not None:
            pygame.draw.rect(screen, "blue", pygame.Rect(cube_pos.x, cube_pos.y, cube_size, cube_size))

    #   movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= movement_speed * dt 
    if keys[pygame.K_s]:
        player_pos.y += movement_speed * dt 
    if keys[pygame.K_a]:
        player_pos.x -= movement_speed * dt 
    if keys[pygame.K_d]:
        player_pos.x += movement_speed * dt 

    #   write to screen
    pygame.display.flip()

pygame.quit()
