import pygame

from snake import Snake
from cube import Cube
from main_menu import MainMenu

class Game:
    def __init__(self):
        #   setup
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("snake")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)

        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.state = "MENU"  # game state
        self.menu_screen = MainMenu(self.width, self.height)
        
        #   initialize objects
        self.snake = Snake(self.width / 4, self.height / 2, 40, 200, self.width, self.height)
        self.cubes = []
        
        self.points = 0
        self.pressedPlay = False
        self.running = True
        
        #   start timer (5 seconds to spawn)
        self.SPAWN_CUBE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPAWN_CUBE_EVENT, 5000)

    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False

        #   state 1: menu handling
        if self.state == "MENU":
            action = self.menu_screen.handle_events(events)
            if action == "PLAY":
                self.state = "PLAYING"
                #   spawns the first cube
                self.cubes.append(Cube(30, self.width, self.height)) 

        #   state 2: gameplay handling
        elif self.state == "PLAYING":
            for event in events:
                if event.type == self.SPAWN_CUBE_EVENT:
                    self.cubes.append(Cube(30, self.width, self.height))

    def update(self, dt):
        if self.state == "MENU":
            self.menu_screen.update(dt)

        elif self.state == "PLAYING":
            keys = pygame.key.get_pressed()
            self.snake.handle_input(keys)
            self.snake.update(dt)

            #   check colisions
            player_hitbox = self.snake.get_rect()
            for cube in self.cubes[:]:
                if player_hitbox.colliderect(cube.rect):
                    self.points += 1
                    self.snake.tail_length += 2
                    self.cubes.remove(cube)

    def draw(self):
        if self.state == "MENU":
            self.menu_screen.draw(self.screen)

        elif self.state == "PLAYING":
            #   background
            self.screen.fill("green")
            #   cubes
            for cube in self.cubes:
                cube.draw(self.screen)
            #   snake
            self.snake.draw(self.screen)
            #   points
            points_text = self.font.render(f"{self.points}", True, (0,0,0))
            points_pos = points_text.get_rect(midtop=(self.width / 2, 10))
            self.screen.blit(points_text, points_pos)

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.draw()
            
        pygame.quit()