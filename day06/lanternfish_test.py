import unittest

from common import read_line_to_ints
from day06.lanternfish import count_fish_after_days


class LanternFishTest(unittest.TestCase):
    test_input = [3, 4, 3, 1, 2]
    input = read_line_to_ints("day06")

    def test_part_1_example(self):
        self.assertEqual(count_fish_after_days(80, self.test_input), 5934)

    def test_part_1_solution(self):
        self.assertEqual(count_fish_after_days(80, self.input), 380243)

    def test_part_2_example(self):
        self.assertEqual(count_fish_after_days(256, self.test_input), 26984457539)

    def test_part_2_solution(self):
        self.assertEqual(count_fish_after_days(256, self.input), 1708791884591)


if __name__ == '__main__':
    unittest.main()
