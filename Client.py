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
selected_answer = ''

# window set-up
window = pygame.display.set_mode((pixel_width, pixel_height))
pygame.display.set_caption("Client")


def game_state0(player):
    player.game_number = database.get_game_number()
    database.player_ready(player.number, player.game_number)
    display_text.display_text("Waiting for more players to connect", window, 500, 500)
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
    if not player.leader:
        player.is_typing = True


def game_state2(player):
    global entered_text

    if player.leader:
        display_text.display_text("Waiting for responses", window, pixel_width, pixel_height)
        database.player_ready(player.number, player.game_number)
        if database.are_players_ready(player.game_number):
            database.next_game_state(player.game_number, player.game_state)
    elif not player.leader and player.is_typing:
        question = database.get_question(player.game_number)
        display_text.display_text("Respond to the following: " + str(question),
                                  window, pixel_width, pixel_height)
        entered_text = player.enter_text(entered_text, 100, 200, window)
    elif not player.leader and not player.is_typing:
        database.insert_user_input(player.number, entered_text, player.game_number)
        database.player_ready(player.number, player.game_number)
        display_text.display_text("Waiting on other players", window, 500, 500)


def game_state4(player):
    global entered_text
    if player.leader and player.is_typing:
        entered_text = player.enter_text(entered_text, 100, 200, window)
    elif player.leader and not player.is_typing:
        if entered_text == 1:
            winner = 1
        elif entered_text == 2:
            winner = 2
        elif entered_text == 3:
            winner = 3
        else:
            display_text.display_text("Invalid response, select again", window, 500, 500)
            player.is_typing = True
        if winner is not None:
            database.set_winner(player.game_number, winner + 1)
            database.next_game_state(player.game_number, player.game_state)
    else:
        display_text.display_text("Waiting on decision", window, 500, 500)
        database.player_ready(player.number, player.game_number)
    if database.are_players_ready(player.game_number):
        database.next_game_state(player.game_number, player.game_number)


def game_state5(player):
    display_text.display_text("The winner is:", window, 500, 500)
    display_text.display_text(database.get_winner(player.game_number), window, 500, 600)
    if player.leader:
        display_text.display_text("Press any key to end game", window, 500, 650)
        temp = player.enter_text(entered_text, 0, 0, window)
        if temp is not None:
            pygame.quit()


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
