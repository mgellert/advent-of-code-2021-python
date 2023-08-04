import unittest
from dataclasses import dataclass
from typing import List

from common import read_lines
from day02.dive import part_1, part_2, parse_commands


@dataclass
class TestCase:
    input: List[str]
    expected: int


class DiveTest(unittest.TestCase):
    input = parse_commands(read_lines("day02"))
    test_input = parse_commands(["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"])

    def test_part_1_example(self):
        self.assertEqual(part_1(self.test_input), 150)

    def test_part_1_solution(self):
        self.assertEqual(part_1(self.input), 1989265)

    def test_part_2_example(self):
        self.assertEqual(part_2(self.test_input), 900)

    def test_part_2_solution(self):
        self.assertEqual(part_2(self.input), 2089174012)


if __name__ == '__main__':
    unittest.main()
