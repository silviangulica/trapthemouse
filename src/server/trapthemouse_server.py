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


def find_game(player):
    for game in games:
        if games[game].player1 == player or games[game].player2 == player:
            return games[game]
    return None


def disconnect_player_from_game(player, game):
    if game.player1 == player:
        game.player1 = None
    else:
        game.player2 = None


def destroy_empty_games():
    global games
    for game in games:
        if games[game].player1 == None and games[game].player2 == None:
            del games[game]
            print(f"Game {game} deleted")
            print(games)
            break


def game_is_not_full_but_started(game):
    return (game.player1 == None or game.player2 == None) and game.game_started


def threaded_client(conn, player_id):
    global games
    global players
    global available_id
    conn.send(str.encode("conn"))
    stop_connection = False
    while not stop_connection:
        try:
            data = conn.recv(2048).decode()
            if data:
                data = data.split(":")
                if data[0] == "make_game":
                    games[player_id] = OnlineGame(
                        game_id=player_id,
                        player1=conn,
                        player2=None,
                    )
                    print(f"Player {player_id} created game {player_id}")
                    reply = {
                        "game_id": player_id,
                        "table": games[player_id].table
                    }
                    conn.sendall(pickle.dumps(reply))
                elif data[0] == "join_game":
                    game_id = int(data[1])
                    if game_id in games:
                        games[game_id].player2 = conn
                        games[game_id].start_game()
                        print(f"Player {player_id} joined game {game_id}")
                        reply = {
                            "game_id": game_id,
                            "table": games[game_id].table
                        }
                        conn.sendall(pickle.dumps(reply))
                    else:
                        conn.sendall(pickle.dumps(None))

                elif data[0] == "move":
                    x = int(data[1])
                    y = int(data[2])
                    for game in games:
                        if games[game].player1 == conn or games[game].player2 == conn:
                            print(f"Player {player_id} made move")
                            games[game].make_move(conn, x, y)

                elif data[0] == "get_table":
                    game = find_game(conn)
                    if game:
                        if game_is_not_full_but_started(game):
                            game.end_game(conn)
                        reply = {
                            "table": game.table,
                            "game_won": game.game_won,
                            "winner": game.winner_name,
                            "my_turn": True if game.player_to_move == conn else False
                        }

                        conn.sendall(pickle.dumps(reply))

                        if game.game_won:
                            disconnect_player_from_game(conn, game)
                            destroy_empty_games()
                            break
                    else:
                        conn.sendall(pickle.dumps(None))

            else:
                break
        except:
            break

    game = find_game(conn)
    if game:
        disconnect_player_from_game(conn, game)
    conn.close()
    del players[player_id]
    print(f"Player {player_id} disconnected")
    available_id = player_id if available_id > player_id else player_id


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    destroy_empty_games()
    if available_id in players:
        available_id += 1
    player_id = available_id
    players[player_id] = conn

    start_new_thread(threaded_client, (conn, player_id))
