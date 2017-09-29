from module.board import Board
from module.player import Player


class Core:
    def __init__(self):
        self.player1 = Player(Board.BLACK, True)
        self.player2 = Player(Board.WHITE, False)
        self.board = Board(8, 8)


    def start(self):
        for i in range(0, 10):
            self.board.show()
            self.player1.choose()
            self.player2.choose()