import pygame
from network import Network
from player import Player
import display_text

pygame.init()

# Global Variables
pixel_width = 500
pixel_height = 500
client_number = 0

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


def read_pos(play_num_str):
    return int(play_num_str)


def make_pos(play_num):
    return str(play_num)


def update_display(text, play1, play2, wind):
    window.fill((0, 0, 0))
    if play1.number == 1:
        display_text.display_text("Enter a question:", wind, 350, 300)
        entered_text = play1.enter_text(text, 150, 200, wind)
    else:
        display_text.display_text("Waiting on group leader input", wind, pixel_width, pixel_height)
        entered_text = ''
    pygame.display.update()
    return entered_text


def main():
    entered_text = ''
    net = Network()
    start_pos = read_pos(net.get_pos())
    play1 = Player(start_pos)
    play2 = Player(start_pos)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        entered_text = update_display(entered_text, play1, play2, window)


main()
