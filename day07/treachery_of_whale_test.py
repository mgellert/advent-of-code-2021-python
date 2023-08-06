import unittest

from common import read_line_to_ints
from day07.treachery_of_whale import find_optimal_pos, constant, \
    increasing


class TreacheryOfWhaleTest(unittest.TestCase):
    test_input = (16, 1, 2, 0, 4, 2, 7, 1, 2, 14)
    input = read_line_to_ints("day07")

    def test_part_1_example(self):
        self.assertEqual(find_optimal_pos(self.test_input, fuel_burn=constant), 37)

    def test_part_1_solution(self):
        self.assertEqual(find_optimal_pos(self.input, fuel_burn=constant), 328318)

    def test_part_2_example(self):
        self.assertEqual(find_optimal_pos(self.test_input, fuel_burn=increasing), 168)

    def test_part_2_solution(self):
        self.assertEqual(find_optimal_pos(self.input, fuel_burn=increasing), 89791146)


if __name__ == '__main__':
    unittest.main()
