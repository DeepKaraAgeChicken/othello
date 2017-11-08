from module.board import Board
from module.player import Player


class Core:
    def __init__(self):
        self.player1 = Player(Board.BLACK, True)
        self.player2 = Player(Board.WHITE, False)
        self.board = Board(4, 4)

    def start(self):
        is_finished = False
        players = (self.player1, self.player2)
        while not is_finished:
            for player in players:
                print(str(player.disc) + "の番")
                self.board.show()
                is_putted = False
                all_puttable_cells = self.board.get_all_puttable_cell(player.disc)
#                if not all_puttable_cells:
#                    print("パスです")
#                    continue
                while not is_putted:
                    chosen_cell = player.choose()
                    print(chosen_cell)
                    is_putted = player.put(self.board, chosen_cell[0], chosen_cell[1])
                    if not is_putted:
                        print("そこには置けません")
                    # TODO このままだとパスできない
        self.board.show()


core = Core()
core.start()
