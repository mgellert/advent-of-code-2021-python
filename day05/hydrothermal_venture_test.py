import unittest

from common import read_lines
from day05.hydrothermal_venture import count_dangerous_areas, parse_lines


class HydrothermalVentureTest(unittest.TestCase):
    test_input = parse_lines((
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
    ))
    input = parse_lines(read_lines("day05"))

    def test_part_1_example(self):
        self.assertEqual(count_dangerous_areas(self.test_input), 5)

    def test_part_1_solution(self):
        self.assertEqual(count_dangerous_areas(self.input), 4826)

    def test_part_2_example(self):
        self.assertEqual(count_dangerous_areas(self.test_input, use_diagonals=True), 12)

    def test_part_2_solution(self):
        self.assertEqual(count_dangerous_areas(self.input, use_diagonals=True), 16793)


if __name__ == '__main__':
    unittest.main()
