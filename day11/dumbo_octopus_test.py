import textwrap
import unittest

from common import read_file
from day11.dumbo_octopus import count_flashes, count_sync, parse_input


class DumboOctopusTest(unittest.TestCase):
    test_input = parse_input(textwrap.dedent("""
            5483143223
            2745854711
            5264556173
            6141336146
            6357385478
            4167524645
            2176841721
            6882881134
            4846848554
            5283751526
            """).strip())
    input = parse_input(read_file("day11"))

    def test_part_1_example(self):
        self.assertEqual(count_flashes(self.test_input), 1656)

    def test_part_1_solution(self):
        self.assertEqual(count_flashes(self.input), 1749)

    def test_part_2_example(self):
        self.assertEqual(count_sync(self.test_input), 195)

    def test_part_2_solution(self):
        self.assertEqual(count_sync(self.input), 285)


if __name__ == '__main__':
    unittest.main()
