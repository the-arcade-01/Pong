import socket
from _thread import *
import pickle
from game import Game

# getting the IP address
server = socket.gethostbyname(socket.gethostname())
# port must be same as that in network
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # bind the server and port
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print('Waiting for a connection, Server Started')

games = {}
idCount = 0

def threaded_client(conn, p, gameId):
    # this is global because it links which player is to be place in which gameId
    global idCount

    # sending data of player p, p is 0 or 1
    conn.send(str.encode(str(p)))

    reply = ""

    while True:
        try:
            # receiving data of a particular player
            data = conn.recv(4096).decode()

            # checking if gameId still exists in games
            if gameId in games:
                game = games[gameId]

                # no data is receive that means connection is lost
                if not data:
                    break
                else:
                    if data == 'reset':
                        game.resetWent()
                    elif data != 'get':
                        game.play(p,data)
                    # send all the
                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    # closing the connection
    print('Lost connection')
    try:
        del games[gameId]
        print('Closing Game', gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    # conn is the new socket object used for sending and receiving data
    conn, addr = s.accept()
    print('Connected to : ', addr)

    # counts the no. of games
    idCount += 1
    # game gets start from player 1
    p = 0
    # gameId stores the count of no. of player in that gameId
    gameId = (idCount - 1)//2
    # each game requires two players if odd then new gameId will be created for that player
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game ...")
    else:
        games[gameId].ready = True
        p = 1

    # starting a new thread for each new connection or player
    start_new_thread(threaded_client,(conn, p, gameId))

