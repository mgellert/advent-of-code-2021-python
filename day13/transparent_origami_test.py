import unittest

from common import read_lines
from day13.transparent_origami import visible_dots_after_first_fold, fold_all


class TransparentOrigamiTest(unittest.TestCase):
    test_input = [
        "6,10",
        "0,14",
        "9,10",
        "0,3",
        "10,4",
        "4,11",
        "6,0",
        "6,12",
        "4,1",
        "0,13",
        "10,12",
        "3,4",
        "3,0",
        "8,4",
        "1,10",
        "2,14",
        "8,10",
        "9,0",
        "",
        "fold along y=7",
        "fold along x=5"]
    input = read_lines("day13")

    def test_part_1_example(self):
        self.assertEqual(visible_dots_after_first_fold(self.test_input), 17)

    def test_part_1_solution(self):
        self.assertEqual(visible_dots_after_first_fold(self.input), 847)

    def test_part_2_example(self):
        print("Day 13 Part 2 Test:")
        print(fold_all(self.test_input))

    def test_part_2_solution(self):
        print("Day 13 Part 2 Solution:")
        print(fold_all(self.input))


if __name__ == '__main__':
    unittest.main()
