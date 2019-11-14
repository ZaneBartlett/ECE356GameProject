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


def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Connection Lost")
    conn.close()


while True:
    conn, addr = sock.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))