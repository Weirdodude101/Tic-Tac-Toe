from Tkinter import *

class TicTacToe(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)
        self.grid(row=0, column=0, sticky=N+S+E+W)

        self.turn = 1

        self.board = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]

        self.buttons = []

    def setup(self):
        for x in xrange(0, 3):
            Grid.rowconfigure(self, x, weight=1)
            for y in xrange(0, 3):
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
            self.turn = (self.turn + 1 if self.turn == 1 else self.turn - 1)

root = Tk()

game = TicTacToe(root)
game.setup()

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)

root.title('Tic Tac Toe')
root.mainloop()
