import socket
import sys
from _thread import *

server = "192.168.0.110"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO make a function to change ports if one does not work
try:
    sock.bind((server, port))
except socket.error as err:
    str(err)

# TODO change 2 to number of players want to play
sock.listen(2)
print("Waiting for connection")
pos = [(0, 0), (100, 100)]
current_players = 0


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = pos[0]
                if player == 0:
                    reply = pos[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Connection Lost")
    conn.close()


def read_pos(pos_str):
    pos_tuple = pos_str.split(",")
    return pos_tuple(str[0]), pos_tuple(str[1])


def make_pos(pos_tuple):
    return str(pos_tuple[0]) + "," + str(pos_tuple[1])


while True:
    conn, addr = sock.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_players))
    current_players += 1
