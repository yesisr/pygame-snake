import pygame
import random

#   setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.Font(None, 50)  # None = default font, 36 = size

pygame.display.set_caption("snake")

#   game properties
width = screen.get_width()
height = screen.get_height()
cube_size = 30
player_size = 40
player_pos = pygame.Vector2(width / 4, height / 2)
movement_speed = 200
direction = pygame.Vector2(1, 0) # starts moving to the right


#region     cube list, event and functions

cubes = []

SPAWN_CUBE_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_CUBE_EVENT, 5000) # 10 sec

def getPosCube():
    # positions with safezones
    x = random.randint(cube_size, width - cube_size)
    y = random.randint(cube_size, height - cube_size)

    pos = pygame.Vector2(x, y)
    print(pos)
    return pos

def spawnCube():
    cube_pos = getPosCube()
    cubes.append(cube_pos)

#endregion

while running:
    #   delta time (60fps)
    dt = clock.tick(60) / 1000

    #   events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_CUBE_EVENT:
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
        #   up (y axis is inverted for screens)
        direction = pygame.Vector2(0, -1)
    if keys[pygame.K_s]:
        #   down (y axis is inverted for screens)
        direction = pygame.Vector2(0, 1)
    if keys[pygame.K_a]:
        #   left
        direction = pygame.Vector2(-1, 0)
    if keys[pygame.K_d]:
        #   right
        direction = pygame.Vector2(1, 0)

    #(calculates x and y axis through the vectors)
    player_pos += direction * movement_speed * dt


    #   borders
    if player_pos.x > width:
        # spawns on the right
        player_pos.x = 0
    if player_pos.x < 0:
        # spawns on the left
        player_pos.x = width
    
    if player_pos.y > height:
        # spawns on the bottom
        player_pos.y = 0
    if player_pos.y < 0:
        # spawns on the top
        player_pos.y = height

    #   points
    points = dt
    points_text = font.render(f"{points}", True, (0,0,0))
    points_pos = points_text.get_rect(midtop=(width / 2, 10))
    screen.blit(points_text, points_pos)

    #   write to screen
    pygame.display.flip()

pygame.quit()


