from othello.module import player


class Core:
    def __init__(self):
        self.player1 = player(board.BLACK, True)
        self.player2 = player(board.WHITE, False)
        self.board = board(8, 8)


    def start(self):
        for i in range(0, 10):
            self.board.show()
            self.player1.choose()
            self.player2.choose()