import pygame
from network import Network
import display_text

pygame.init()

# Global Variables
pixel_width = 500
pixel_height = 500
client_number = 0
entered_text = ''

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


def game_state0(player):
    global entered_text
    if player.leader and player.is_typing:
        display_text.display_text("Enter a question:", window, 350, 300)
        entered_text = player.enter_text(entered_text, 100, 200, window)
    elif player.leader and not player.is_typing:
        player.question = entered_text
        player.game_state += 1
    else:
        display_text.display_text("Waiting on other players", window, pixel_width, pixel_height)


def game_state1(player):
    global entered_text
    if player.leader:
        display_text.display_text("Waiting for responses", window, pixel_width, pixel_height)
    elif not player.leader:
        display_text.display_text("Respond to the following: " + player.question, window, pixel_width, pixel_height)
        entered_text = player.enter_text(entered_text, 100, 200, window)


def update_display(player):
    window.fill((0, 0, 0))
    if player.game_state == 0:
        game_state0(player)
    elif player.game_state == 1:
        game_state1(player)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    net = Network()
    player1 = net.get_player()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        update_display(player1)


main()
