import pygame
from network import Network

# Global Variables
pixel_width = 500
pixel_height = 500
client_number = 0

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


class Player:
    def __init__(self, x, y, width, height, colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.rect = (x, y, width, height)
        self.vel = 1

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


def read_pos(pos_str):
    pos_tuple = pos_str.split(",")
    return pos_tuple(str[0]), pos_tuple(str[1])


def make_pos(pos_tuple):
    return str(pos_tuple[0]) + "," + str(pos_tuple[1])


def update_display(player, player2, wind):
    window.fill((0, 0, 0))
    player.draw_player(wind)
    player2.draw(wind)
    pygame.display.update()


def main():
    run = True
    net = Network()
    start_pos = read_pos(net.get_pos())
    player = Player(start_pos[0], start_pos[1], 100, 100, (255, 255, 255))
    player2 = Player(0, 0, 100, 100, (255, 255, 255))
    while run:
        player2_pos = read_pos(net.send(make_pos((player.x, player.y))))
        player2.x = player2_pos[0]
        player2.y = player2_pos[1]
        player2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move_player()
        update_display(player, player2, window)


main()


