import pygame
from ui.button import Button

class MainMenu:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height

        #   title
        self.font = pygame.font.Font(None, 80)
        self.text = self.font.render("Snake", True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.width / 2, self.height / 3))

        #   play button
        button_width, button_height = 220, 60
        button_x = (self.width / 2) - (button_width / 2)
        button_y = self.height / 1.5
        
        self.play_button = Button(button_x, button_y, button_width, button_height, "PLAY")

    def handle_events(self, events):
        """starts the game if player presses the button or spacebar"""
        for event in events:
            #   player clicks the button
            if self.play_button.handle_event(event):
                return "PLAY"
            
            #   player presses spacebar
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "PLAY"
        return "MENU"

    def update(self, dt):   #   static right now
        pass    

    def draw(self, screen):
        screen.fill("green")
        screen.blit(self.text, self.text_rect)
        self.play_button.draw(screen)