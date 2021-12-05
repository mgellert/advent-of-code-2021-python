import textwrap
import unittest

from day04.giant_squid import BingoBoard, calculate_first_winner, calculate_last_winner


class TestGiantSquid(unittest.TestCase):
    def test_board_init(self):
        bingo = BingoBoard(textwrap.dedent("""
            22 13 17 11  0
             8  2 23  4 24
            21  9 14 16  7
             6 10  3 18  5
             1 12 20 15 19"""))
        self.assertEqual(bingo.board, [
            [22, 13, 17, 11, 0],
            [8, 2, 23, 4, 24],
            [21, 9, 14, 16, 7],
            [6, 10, 3, 18, 5],
            [1, 12, 20, 15, 19]
        ])

    def test_mark(self):
        bingo = BingoBoard(textwrap.dedent("""
                    14 21 17 24  4
                    10 16 15  9 19
                    18  8 23 26 20
                    22 11 13  6  5
                     2  0 12  3  7"""))
        draws = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21]
        for draw in draws:
            res = bingo.mark(draw)
            self.assertIsNone(res)
        res = bingo.mark(24)
        self.assertEqual(res, 4512)

    def test_calculate_first_winner(self):
        got = calculate_first_winner()
        expected = 39984
        self.assertEqual(got, expected)

    def test_calculate_last_winner(self):
        got = calculate_last_winner()
        expected = 8468
        self.assertEqual(got, expected)


if __name__ == '__main__':
    unittest.main()
