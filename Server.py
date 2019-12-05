import socket
from _thread import *
from player import Player
import pickle
import database

server = "10.0.0.151"
port = 5555

# initialize a socket to connect to through the internet
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the ip address and port for the server
try:
    sock.bind((server, port))
except socket.error as err:
    str(err)

# begin listening for connections to the socket
# 4 connections will allow for for players, this can be varied to allow for more players
sock.listen(4)
print("Waiting for connection")

# initialize 4 players in an array to make it easy for players to connect,
# if want more players add more inits, first value is the player number,
# second determines if they are the leader
players = [Player(1, True), Player(2, False), Player(3, False), Player(4, False)]

# variable to keep track of the current number of players
current_number_of_players = 0


# this function will switch the leader to the next player in the array when called
def leader_change(current_leader_num):
    players[current_leader_num].leader = False
    current_leader_num = (current_leader_num + 1) % 4
    players[current_leader_num].leader = True


# a function to create a new player client and begin communications when called
def threaded_client(conn, player):
    if player == 0:
        database.new_game()
    players[player].game_number = database.get_game_number()
    # send the current player initialization to Client.py
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            # make sure we receive a proper reply and update the current player
            # values correspondingly
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                # update the current player with the rest of the player's info
                if player > 0:
                    reply = players[0]
                if player == 0:
                    reply = players[1]
                print("Received: ", data)
                print("Sending: ", reply)

            # send a reply with the data the player needs
            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection Lost")
    conn.close()


# infinite loop to add more players and start new threads for them as they join
while True:
    conn, addr = sock.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_number_of_players))
    current_number_of_players += 1
