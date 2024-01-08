from _thread import *
import socket
import pickle
from onlinegame import OnlineGame

server = "127.0.0.1"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)

print("Waiting for a connection, Server Started")


games = {}
available_id = 0
players = {}

'''
    Protocul UBRA:
    - make_game:player_mode
    - join_game:game_id
    - move:y:x
'''


def threaded_client(conn, player_id):
    global games
    global players
    global available_id
    conn.send(str.encode("conn"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048).decode()
            if data:
                data = data.split(":")
                if data[0] == "make_game":
                    games[player_id] = OnlineGame(
                        game_id=player_id,
                        player1=player_id,
                        player2=None,
                        game_type=data[1]
                    )
                    reply = "game_created"
                    conn.sendall(str.encode(reply))
                    conn.sendall(pickle.dumps(games[player_id].table))
                elif data[0] == "join_game":
                    pass
            else:
                break
        except:
            pass
    conn.close()
    del players[player_id]
    print(f"Player {player_id} disconnected")
    available_id = player_id


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    if available_id in players:
        available_id += 1
    player_id = available_id
    players[player_id] = conn

    start_new_thread(threaded_client, (conn, player_id))
