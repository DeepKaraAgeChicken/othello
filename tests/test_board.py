import unittest

from module.board import Board


class TestBoard(unittest.TestCase):

    def test1(self):
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

    def test2(self):
        self.assertEqual(1,1)
        print('test2')

    def func(self):
        print('func')


if __name__ == "__main__":
    unittest.main()