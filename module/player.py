from module.board import Board


class Player:
    def __init__(self, disc: int, is_attack_first):
        self.disc = disc
        self.is_attack_first = is_attack_first

    def choose(self):
        print("X座標を入力してね")
        x = int(input())
        print("Y座標を入力してね")
        y = int(input())
        return [x, y]

    def put(self, board: Board, x: int, y: int):
        if board.is_puttable(self.disc, x, y):
            board.put_disc(self.disc, x, y)
            return True
        else:
            return False


class AIPlayer(Player):
    def choose(self):
        pass