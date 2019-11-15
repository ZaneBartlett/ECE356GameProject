import pygame


class Player:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = 1
        self.leader = False

    def draw_player(self, wind):
        pygame.draw.rect(wind, self.colour, self.rect)

    def move_player(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.x != 0:
            self.x -= self.vel
        if key[pygame.K_RIGHT] and self.x != 400:
            self.x += self.vel
        if key[pygame.K_UP] and self.y != 0:
            self.y -= self.vel
        if key[pygame.K_DOWN] and self.y != 400:
            self.y += self.vel
        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
