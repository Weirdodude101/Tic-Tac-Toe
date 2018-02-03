from tkinter import *
from tkinter import messagebox
import sys


class TicTacToe(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(row=0, column=0, sticky=N+S+E+W)

        self.turn = 1
        self.round = 0
        self.board = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]

        self.winCombos = [[0,1,2],[3,4,5],[6,7,8],
                          [0,3,6],[1,4,7],[2,5,8],
                          [0,4,8],[2,4,6]]

        self.buttons = []

    def setup(self):
        for x in range(0, 3):
            Grid.rowconfigure(self, x, weight=1)
            for y in range(0, 3):
                Grid.columnconfigure(self, y, weight=1)
                button = Button(self)
                button.pack()
                button.grid(row=x, column=y, sticky=N+S+E+W)
                self.buttons.append(button)

        for button in self.buttons:
            button.configure(command=lambda x=self.buttons.index(button):self.place(x))

    def place(self, val):
        if self.board[val] == 0:
            self.buttons[val].configure(text=('X' if self.turn == 1 else 'O'))
            self.board[val] = self.turn
            self.checkWin(val)
            self.round += 1
            self.turn = (self.turn + 1 if self.turn == 1 else self.turn - 1)

    def checkWin(self, val):
        option = None
        for x in self.winCombos:
            if val in x:
                if self.board[x[0]] == self.turn and self.board[x[1]] == self.turn and self.board[x[2]] == self.turn:
                    player = ('X' if self.turn == 1 else 'O')
                    option = messagebox.askyesno('%s WINS!' % player, "%s has won the game.\nWould you like to play again?" % player)
                else:
                    if self.round >= 9:
                        option = messagebox.askyesno('TIE!', "There has been a tie\nWould you like to play again?")

                if option != None:
                    if not option:
                        sys.exit()
                    self.reset()



    def reset(self):
        for x in range(0,len(self.board)):
            self.board[x] = 0
            self.buttons[x].configure(text='')
            self.turn = (self.turn + 1 if self.turn == 1 else self.turn - 1)
            self.round = 0




root = Tk()

game = TicTacToe(root)
game.setup()

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

root.title('Tic Tac Toe')
root.mainloop()
