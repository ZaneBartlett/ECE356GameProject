import pygame
from network import Network
import display_text
import database

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
    player.game_number = database.get_game_number()
    database.player_ready(player.number, player.game_number)
    display_text.display_text("Waiting for more players to connect", window, 500, 500)
    print(database.are_players_ready(player.game_number))
    if database.are_players_ready(player.game_number):
        database.next_game_state(player.game_number, player.game_state)
    player.game_state = database.get_game_state(player.game_number)


def game_state1(player):
    global entered_text
    if player.leader and player.is_typing:
        display_text.display_text("Enter a question:", window, 350, 300)
        entered_text = player.enter_text(entered_text, 100, 200, window)
    elif player.leader and not player.is_typing:
        database.insert_user_input(player.number, entered_text, player.game_number)
        database.next_game_state(player.game_number, player.game_state)
    else:
        display_text.display_text("Waiting on input", window, pixel_width, pixel_height)

    player.game_state = database.get_game_state(player.game_number)


def game_state2(player):
    global entered_text
    if player.leader:
        display_text.display_text("Waiting for responses", window, pixel_width, pixel_height)
        database.player_ready(player.number, player.game_number)
    elif not player.leader and player.is_typing:
        display_text.display_text("Respond to the following: " + database.get_question(player.game_number),
                                  window, pixel_width, pixel_height)
        entered_text = player.enter_text(entered_text, 100, 200, window)
    elif not player.leader and not player.is_typing:
        database.insert_user_input(player.number, entered_text, player.game_number)
        database.player_ready(player.number, player.game_number)
    elif database.are_players_ready(player.game_number):
        database.next_game_state(player.game_number, player.game_state)
    else:
        display_text.display_text("Waiting on other players", window, 500, 500)


def game_state3(player):
    display_text.display_text("not implemented yet", window, 500, 500)


def update_display(player):
    window.fill((0, 0, 0))
    if player.game_state == 0:
        game_state0(player)
    elif player.game_state == 1:
        game_state1(player)
    elif player.game_state == 2:
        game_state2(player)
    elif player.game_state == 3:
        game_state3(player)
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
