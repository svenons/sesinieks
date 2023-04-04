import PySimpleGUI as sg
import random

class Game:
    def __init__(self):
        layout = [
                [sg.Text('Player1: '), sg.Input(key='i1')],
                [sg.Text('Player2: '), sg.Input(key='i2')],
                [sg.Text('Player3: '), sg.Input(key='i3')],
                [sg.Text('Player4: '), sg.Input(key='i4')],
                [sg.Text('Player5: '), sg.Input(key='i5')],
                [sg.Text('Player6: '), sg.Input(key='i6')],
                [sg.Button('Submit', key='submit')]
            ]

        window = sg.Window('Enter names for players', layout, finalize=True)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                exit()
            elif event == 'submit':
                window.close()
                break
        self.players = {}
        for x in values:
            if not values[x] == '':
                self.players[values[x]] = 4
                self.playercount = len(self.players)
    def board(self, playernames):
        players = []
        for x in playernames:
            players.append([x, playernames[x]])
        self.colors = ['red', 'green', 'blue', 'orange', 'purple', 'pink']
        self.dots = [False] * 6
        layout = [
            [sg.Push(), sg.Text('rolled number x', key='gametext', visible=False), sg.Push()],
            [sg.Push(), sg.Text('Players:'), sg.Push()],
            [sg.Push(), sg.Table(values=players, headings=['Name', 'Trophies'], auto_size_columns=True, key='players', enable_events=True), sg.Push()],
            [sg.Push(), sg.Button('Start game', key='start'), sg.Push()],
            [sg.Push(), sg.Button('Roll dice', key='dice', visible=False), sg.Push()],
            [sg.Push(), sg.Button('Place trophy', key='place', visible=False), sg.Push()],
            [sg.Push(), sg.Button('Take trophy', key='take', visible=False), sg.Push()],
            [sg.Canvas(size=(150, 150), background_color='red', key='canvas1'), sg.Canvas(size=(150, 150), background_color='green', key='canvas2'), sg.Canvas(size=(150, 150), background_color='yellow', key='canvas3')],
            [sg.Canvas(size=(150, 150), background_color='blue', key='canvas4'), sg.Canvas(size=(150, 150), background_color='purple', key='canvas5'), sg.Canvas(size=(150, 150), background_color='orange', key='canvas6')],
        ]

        window = sg.Window('Game Six', layout, finalize=True)

        self.cir1 = window['canvas1'].TKCanvas.create_oval(50, 50, 100, 100)
        self.cir2 = window['canvas2'].TKCanvas.create_oval(50, 50, 100, 100)
        self.cir3 = window['canvas3'].TKCanvas.create_oval(50, 50, 100, 100)
        self.cir4 = window['canvas4'].TKCanvas.create_oval(50, 50, 100, 100)
        self.cir5 = window['canvas5'].TKCanvas.create_oval(50, 50, 100, 100)
        self.cir6 = window['canvas6'].TKCanvas.create_oval(50, 50, 100, 100)
        self.cirlist = {1: self.cir1, 2:self.cir2, 3:self.cir3, 4:self.cir4, 5:self.cir5, 6:self.cir6}

        self.window = window
        self.moves = 0
        self.window['start'].Update(visible=True)
        self.board = [0,0,0,0,0,0]
        self.gameEnded = False
    def play(self):
        if self.window['start'].visible == True:
            while True:
                event, values = self.window.read()
                if event == sg.WIN_CLOSED:
                    break
                elif event == 'start':
                    self.window['start'].Update(visible=False)
                    break
        for x in self.players:
            self.gameEnded = False
            self.window['dice'].Update(visible=True)
            self.window['gametext'].Update(f'Player {x} needs to roll the dice!', visible=True)
            do = True
            while do == True:
                if not self.gameEnded:
                    event, values = self.window.read()
                    self.moves += 1
                    if event == sg.WIN_CLOSED:
                        break
                    elif event == 'dice':
                        self.window['dice'].Update(visible=False)
                        number = random.randrange(0, 5) + 1

                        if self.board[number] == 0:
                            self.window['place'].Update(visible=True)
                            self.window['gametext'].Update(f'Player {x} rolled {number} and should place the trophy!')
                        else:
                            self.window['take'].Update(visible=True)
                            self.window['gametext'].Update(f'Player {x} rolled {number} and should take the trophy!')
                            self.board[number] = 0
                    
                    elif event == 'place':
                        self.board[number] = 1
                        self.players[x] = self.players[x] - 1
                        self.window['place'].Update(visible=False)
                        self.window[f'canvas{number}'].TKCanvas.itemconfig(self.cirlist[number], fill='black')
                        if self.players[x] == 0:
                            sg.Popup(x, 'won!')
                            do = False
                            self.gameEnded = True
                            return
                        players = []
                        for x in self.players:
                            players.append([x, self.players[x]])
                        self.window['players'].Update(players)
                        do = False
                    
                    elif event == 'take':
                        self.window['take'].Update(visible=False)
                        self.window[f'canvas{number}'].TKCanvas.itemconfig(self.cirlist[number], fill='white')
                        do = False
                else:
                    self.window.close()

while True:
    game = Game()
    if not len(game.players) < 2:
        break
    else:
        sg.Popup('Each name must be unique and at least 2 players should participate!')
game.board(game.players)
while not game.gameEnded:
    game.play()
