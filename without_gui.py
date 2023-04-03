# GAME SIX
import random

board = [0,0,0,0,0,0] #0 - empty, 1 - taken

playercount = 6 #2-6v
players = {}

for x in range(0, playercount):
    while True:
        name = input('Enter name: ')
        players[name] = 4
        if not name == '':
            break

moves = 0
won = False

while won == False:
    for x in players:
        moves += 1
        number = random.randrange(0, 5)
        print(x, 'rolled number ', number)
        if board[number] == 0:
            board[number] = 1
            players[x] = players[x] - 1
            print('Player', x, 'placed a trophy on', number)
        else:
            board[number] = 0
            print('Player', x, 'placed trophy on', number)
        if players[x] == 0:
            print(x, 'won!')
            won = True
            break
    

print('Total moves:', moves)