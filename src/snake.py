import pygame

head_color = "red"
tail_color = "blue"

class Snake:
    def __init__(self, start_x, start_y, size, speed, screen_width, screen_height):
        self.pos = pygame.Vector2(start_x, start_y)
        self.size = size
        self.speed = speed
        self.direction = pygame.Vector2(1, 0)
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        #   tail properties
        self.pos_history = []
        self.tail_length = 0
        self.segment_spacing = 10 # 10 snapshots

    def get_rect(self):
        """returns the head hitbox"""
        return pygame.Rect(self.pos.x, self.pos.y, self.size, self.size)

    def handle_input(self, keys):
        """changes directions"""
        if keys[pygame.K_w]:
            self.direction = pygame.Vector2(0, -1)
        if keys[pygame.K_s]:
            self.direction = pygame.Vector2(0, 1)
        if keys[pygame.K_a]:
            self.direction = pygame.Vector2(-1, 0)
        if keys[pygame.K_d]:
            self.direction = pygame.Vector2(1, 0)

    def update(self, dt):
        """handles movement and warparound"""
        #   calculate x and y through vectors
        self.pos += self.direction * self.speed * dt
        
        #   warparound
        if self.pos.x > self.screen_width: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = self.screen_width
        if self.pos.y > self.screen_height: self.pos.y = 0
        if self.pos.y < 0: self.pos.y = self.screen_height
        
        #   insert pos in pos history
        self.pos_history.insert(0, pygame.Vector2(self.pos.x, self.pos.y))

        #   trim position list to avoid memory problems
        max_needed = (self.tail_length + 1) * self.segment_spacing #    +1 because tail can be 0
        self.pos_history = self.pos_history[:max_needed]

    def draw(self, screen):
        """renders the head and the tail"""
        #   tail
        for i in range(1, self.tail_length + 1):
            index = i * self.segment_spacing
            if index < len(self.pos_history):
                seg_pos = self.pos_history[index]
                pygame.draw.rect(screen, tail_color, pygame.Rect(seg_pos.x, seg_pos.y, self.size, self.size))
        
        #   head
        pygame.draw.rect(screen, head_color, self.get_rect())