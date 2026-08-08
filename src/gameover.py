import pygame
from ui.button import Button

title_text = "GAME OVER"
replay_text = "REPLAY"

class GameOver:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height

        #   semi transparent overlay 160 alpha
        self.overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.overlay.fill((0, 0, 0, 160)) 

        self.title_font = pygame.font.Font(None, 80)
        self.score_font = pygame.font.Font(None, 45)

        #   text
        self.title_text = self.title_font.render(title_text, True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.width / 2, self.height / 3))

        #   replay button
        button_width, button_height = 220, 60
        button_x = (self.width / 2) - (button_width / 2)
        button_y = self.height / 1.6
        self.play_button = Button(button_x, button_y, button_width, button_height, replay_text)

    def handle_events(self, events):
        for event in events:
            if self.play_button.handle_event(event):
                return "PLAY"
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return "PLAY"
        return "GAMEOVER"

    def update(self, dt):
        pass

    def draw(self, screen, final_score):
        screen.blit(self.overlay, (0, 0))
        screen.blit(self.title_text, self.title_rect)

        #   final score
        score_text = self.score_font.render(f"SCORE: {final_score}", True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(self.width / 2, self.height / 2))
        screen.blit(score_text, score_rect)

        #   restart button
        self.play_button.draw(screen)