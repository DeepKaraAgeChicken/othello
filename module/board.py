import numpy as np


class Board:
    BLACK = -1
    WHITE = 1
    EMPTY = 0

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = np.zeros(width * height).reshape(height, width)
        self.board[height // 2][width // 2] = Board.BLACK
        self.board[height // 2 - 1][width // 2] = Board.WHITE
        self.board[height // 2][width // 2 - 1] = Board.WHITE
        self.board[height // 2 - 1][width // 2 - 1] = Board.BLACK

    def put_disc(self, disc: int, x: int, y: int):
        """
        石を置いてひっくりかえす。無理なら例外を投げる。
        :param disc: 石の色。1か-1を渡すこと。
        :param x: X座標。配列のインデックスとして渡すこと(0始まり)
        :param y: Y座標。X座標と同様。
        :return:
        """
        if not self._is_inside(x, y):
            raise ValueError("盤面の範囲外なので置けない")
        if self.board[y][x] != 0:
            raise ValueError("すでに他の石があるので置けない")
        is_putted = False
        for vx in range(-1, 2):
            for vy in range(-1, 2):
                if self.board[y + vy][x + vx] == -disc:
                    # vx, vyは方向を表す。-1～1として、9方向を表現する
                    if self._turn_recursive(disc, y, x, vy, vx):
                        # ひっくりかえせる場合はそこに石を置ける
                        self.board[y][x] = disc
                        is_putted = True
        if not is_putted:
            raise ValueError("その座標には石を置けない(取れる石がない)")

    def _turn_recursive(self, disc: int, x: int, y: int, vx: int, vy: int) -> bool:
        next_x = x + vx
        next_y = y + vy
        if not self._is_inside(next_x, next_y):
            # 範囲外に出たらだめ
            return False
        next_disc = self.board[next_x][next_y]
        if next_disc == self.EMPTY:
            # 隣に石がない場合もだめ
            return False
        elif next_disc == disc:
            # 隣が自分の石ならそこまでのやつを全部ひっくりかえせる
            return True
        elif next_disc != disc:
            # 隣が相手の石なら、さらにその隣の石も見る
            if self._turn_recursive(disc, next_x, next_y, vx, vy):
                self.board[next_x][next_y] = disc
                return True
        return False

    def _is_inside(self, x: int, y: int):
        return 0 <= x < self.width and 0 <= y < self.height

    def show(self):
        x = 0
        y = 0
        for row in self.board:
            for cell in row:
                if cell == Board.BLACK:
                    print("●", end="")
                elif cell == Board.WHITE:
                    print("〇", end="")
                else:
                    if self.is_puttable(cell, x, y):
                        print("■", end="")
                    else:
                        print("□", end="")
            print("")
            y += 1
        print("")
        x += 1

    def is_puttable(self, disk: int, x: int, y: int):
        target_sell = self.board[y][x]
        if target_sell != self.EMPTY:
            return False
        for vx in range(-1, 2):
            for vy in range(-1, 2):
                if self._is_puttable_recursive(disk, x, y, vx, vy):
                    return True
        return False

    def _is_puttable_recursive(self, disc: int, x: int, y: int, vx: int, vy: int):
        next_x = x + vx
        next_y = y + vy
        if not self._is_inside(next_x, next_y):
            # 範囲外に出たらだめ
            return False
        next_disc = self.board[next_x][next_y]
        if next_disc == self.EMPTY:
            # 隣に石がない場合もだめ
            return False
        elif next_disc == disc:
            # 隣が自分の石ならそこまでのやつを全部ひっくりかえせる
            return True
        elif next_disc != disc:
            # 隣が相手の石なら、さらにその隣の石も見る
            return self._turn_recursive(disc, next_x, next_y, vx, vy)

    def get_all_puttable_cell(self, disc: int):
        puttable_cells = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self.is_puttable(disc, x, y):
                    puttable_cells.append([x, y])
        return puttable_cells


b = Board(6, 6)
b.show()
b.put_disc(Board.WHITE, 1, 2)
b.show()
b.put_disc(Board.BLACK, 1, 1)
b.show()
b.put_disc(Board.WHITE, 2, 1)
b.show()
b.put_disc(Board.BLACK, 1, 3)
b.show()
b.put_disc(Board.WHITE, 0, 3)
b.show()
b.put_disc(Board.BLACK, 3, 1)
b.show()
b.put_disc(Board.WHITE, 4, 3)
b.show()
