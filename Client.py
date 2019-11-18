import pygame
from network import Network
import display_text

pygame.init()

# Global Variables
pixel_width = 500
pixel_height = 500
client_number = 0

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


def update_display(text, player1, wind):
    window.fill((0, 0, 0))
    if player1.leader and player1.is_typing:
        display_text.display_text("Enter a question:", wind, 350, 300)
        player1.enter_text(text, 100, 200, wind)
    elif player1.leader and not player1.is_typing:
        display_text.display_text("Waiting on player responses", wind, pixel_width, pixel_height)
    elif not player1.leader and player1.is_typing:
        display_text.display_text("Respond to the following: " + text, wind, pixel_width, pixel_height)
        player1.enter_text(text, 100, 200, wind)
    else:
        display_text.display_text("Waiting on other players", wind, pixel_width, pixel_height)

    pygame.display.update()
    return player1.last_entered_text


def main():
    clock = pygame.time.Clock()
    net = Network()
    player1 = net.get_player()
    entered_text = ''
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        entered_text = update_display(entered_text, player1, window)


main()
