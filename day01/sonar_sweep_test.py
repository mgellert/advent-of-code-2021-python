import unittest

from common import read_file_to_ints
from day01.sonar_sweep import part_1, part_2


class SonarSweepTest(unittest.TestCase):
    def test_part_1_example(self):
        measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(part_1(measurements), 7)

    def test_part_1_solution(self):
        measurements = read_file_to_ints("day01")
        self.assertEqual(part_1(measurements), 1832)

    def test_part_2_example(self):
        measurements = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(part_2(measurements), 5)

    def test_part_2_solution(self):
        measurements = read_file_to_ints("day01")
        self.assertEqual(part_2(measurements), 1858)


if __name__ == '__main__':
    unittest.main()
