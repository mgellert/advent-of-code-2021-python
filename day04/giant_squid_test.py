import textwrap
import unittest

from common import read_file
from day04.giant_squid import BingoBoard, part_1, part_2, parse_input


class TestGiantSquid(unittest.TestCase):
    draws, boards = parse_input(read_file("day04"))

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
            bingo.mark(draw)
            self.assertFalse(bingo.is_winner())

        bingo.mark(24)
        self.assertTrue(bingo.is_winner())
        self.assertEqual(bingo.score() * 24, 4512)

    def test_part_1_solution(self):
        self.assertEqual(part_1(self.draws, self.boards), 39984)

    def test_part_2_solution(self):
        self.assertEqual(part_2(self.draws, self.boards), 8468)


if __name__ == '__main__':
    unittest.main()
