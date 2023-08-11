import textwrap
import unittest

from common import read_file
from day09.smoke_basin import part_1, part_2, parse_input


class TestSmokeBasin(unittest.TestCase):
    test_input = parse_input(textwrap.dedent(
        """
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
        """).strip())
    input = parse_input(read_file("day09"))

    def test_part_1_example(self):
        self.assertEqual(part_1(self.test_input), 15)

    def test_part_1_solution(self):
        self.assertEqual(part_1(self.input), 524)

    def test_part_2_example(self):
        self.assertEqual(part_2(self.test_input), 1134)

    def test_part_2_solution(self):
        self.assertEqual(part_2(self.input), 1235430)


if __name__ == '__main__':
    unittest.main()
