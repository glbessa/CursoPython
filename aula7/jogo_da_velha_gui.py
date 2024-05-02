import threading

import tkinter
from tkinter import Tk, ttk, Button, Frame, Label

class JogoDaVelhaGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title('Jogo da Velha')
        self.geometry('300x300')
        # Coloque o codigo de inicialização aqui
        self.rodada = 'x'

        self.font = ('Arial', 12)

        self._build_grid()
        self.grid.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.player_round_lbl = Label(self, text='Vez do jogador: X', font=self.font)
        self.player_round_lbl.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    def _build_grid(self):
        self.grid = Frame(self)
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = Button(self.grid, text=' ', width=2, height=1, font=self.font, command=lambda i=i, j=j: self._on_button_click(i, j))
                button.grid(row=i, column=j, sticky='nsew')
                row.append(button)
            self.buttons.append(row)

    def _on_button_click(self, i, j):
        """
        Lógica principal do jogo!
        """



        self.buttons[i][j].config(text=self.rodada)

    """
    Coloque o resto do seu codigo aqui
    """


if __name__ == '__main__':
    window = JogoDaVelhaGUI()
    window.mainloop()
    #t = threading.Thread(target=window.mainloop)
    #t.start()
    #t.join()