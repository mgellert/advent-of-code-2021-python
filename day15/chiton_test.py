import unittest

from common import read_lines
from day15.chiton import find_lowest_total_risk_path, find_lowest_total_risk_path_in_large_cavern


class ChitonTest(unittest.TestCase):
    test_input = [
        "1163751742",
        "1381373672",
        "2136511328",
        "3694931569",
        "7463417111",
        "1319128137",
        "1359912421",
        "3125421639",
        "1293138521",
        "2311944581"
    ]
    input = read_lines("day15")

    def test_part_1_example(self):
        self.assertEqual(find_lowest_total_risk_path(self.test_input), 40)

    def test_part_1_solution(self):
        self.assertEqual(find_lowest_total_risk_path(self.input), 390)

    def test_part_2_example(self):
        self.assertEqual(find_lowest_total_risk_path_in_large_cavern(self.test_input), 315)

    def test_part_2_solution(self):
        self.assertEqual(find_lowest_total_risk_path_in_large_cavern(self.input), 2814)


if __name__ == '__main__':
    unittest.main()
