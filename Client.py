import pygame
from network import Network

# Global Variables
pixel_width = 500
pixel_height = 500
client_number = 0

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


class Player():
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = 1

    def draw_player(self, window):
        pygame.draw.rect(window, self.colour, self.rect)

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
        self.rect = (self.x, self.y, self.width, self.height)


def update_display(player, window):
    window.fill((0, 0, 0))
    player.draw_player(window)
    pygame.display.update()


def main():
    run = True
    net = Network()
    startPos = net.get_pos()
    player = Player(50, 50, 100, 100, (255, 255, 255))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move_player()
        update_display(player, window)

main()


