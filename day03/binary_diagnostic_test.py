import unittest
from dataclasses import dataclass
from typing import List

from common import read_lines
from day03.binary_diagnostic import part_1, part_2


@dataclass
class TestCase:
    input: List[str]
    expected: int


class BinaryDiagnosticTest(unittest.TestCase):
    test_input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010",
                  "01010"]
    input = read_lines("day03")

    def test_part_1_example(self):
        self.assertEqual(part_1(self.test_input), 198)

    def test_part_1_solution(self):
        self.assertEqual(part_1(self.input), 3847100)

    def test_part_2_example(self):
        self.assertEqual(part_2(self.test_input), 230)

    def test_part_2_solution(self):
        self.assertEqual(part_2(self.input), 4105235)


if __name__ == '__main__':
    unittest.main()
