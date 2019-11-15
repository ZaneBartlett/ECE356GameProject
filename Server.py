import socket
from _thread import *

server = "134.87.148.149"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# TODO make a function to change ports if one does not work
try:
    sock.bind((server, port))
except socket.error as err:
    str(err)

sock.listen(4)
print("Waiting for connection")
play_nums = [1, 2, 3, 4, 5, 6, 7, 8]
current_players = 0


def threaded_client(conn, player):
    conn.send(str.encode(make_pos(play_nums[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            play_nums[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player > 0:
                    reply = play_nums[0]
                if player == 0:
                    reply = play_nums[1]
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(str.encode(make_pos(reply)))
        except:
            break

    print("Connection Lost")
    conn.close()


def read_pos(play_num_str):
    return int(play_num_str)


def make_pos(play_num):
    return str(play_num)


while True:
    conn, addr = sock.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, current_players))
    current_players += 1
