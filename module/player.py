from othello.module import board


class Player:
    def __init__(self, disc: int, is_attack_first):
        self.disc = disc
        self.is_attack_first = is_attack_first


    def choose(self):
        x = input()
        y = input()
        return [x, y]

    def put(self, board: board, x: int, y: int):
        board.put_disc(self.disc, x, y)

