import pygame
from network import Network
from player import Player
import display_text
import enter_text

pygame.init()

# Global Variables
pixel_width = 500
pixel_height = 500
client_number = 0

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


def read_pos(pos_str):
    pos_str = pos_str.split(",")
    return int(pos_str[0]), int(pos_str[1])


def make_pos(pos_tuple):
    return str(pos_tuple[0]) + "," + str(pos_tuple[1])


def update_display(text, play1, play2, wind):
    window.fill((0, 0, 0))
    # play1.draw_player(wind)
    # play2.draw_player(wind)
    if play1.x == 0 and play1.y == 0:
        display_text.display_text("Enter a question here:", wind, 250, 100)
        entered_text = enter_text.enter_text(text, 100, 100, wind)
    else:
        display_text.display_text("Waiting on group leader input", wind, pixel_width, pixel_height)
        entered_text = ''
    pygame.display.update()
    return entered_text


def main():
    entered_text = ''
    net = Network()
    start_pos = read_pos(net.get_pos())
    play1 = Player(start_pos[0], start_pos[1], 100, 100, (255, 0, 0))
    play2 = Player(0, 0, 100, 100, (0, 255, 0))
    while True:
        player2_pos = read_pos(net.send(make_pos((play1.x, play1.y))))
        play2.x = player2_pos[0]
        play2.y = player2_pos[1]
        play2.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        play1.move_player()
        entered_text = update_display(entered_text, play1, play2, window)


main()
