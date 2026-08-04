import pygame
import random

color = "blue"

class Cube:
    def __init__(self, size, screen_width, screen_height):
        self.size = size
        #   pos with safezones
        self.x = random.randint(size, screen_width - size)
        self.y = random.randint(size, screen_height - size)

        #   hitbox
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def draw(self, screen):
        pygame.draw.rect(screen, color, self.rect)