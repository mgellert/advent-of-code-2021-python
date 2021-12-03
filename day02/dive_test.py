import unittest
from dataclasses import dataclass
from typing import List

from day02.dive import calculate_position, read_file, calculate_aim


@dataclass
class TestCase:
    input: List[str]
    expected: int


class DiveTest(unittest.TestCase):
    def test_calculate_position(self):
        testcases = [
            TestCase(input=["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], expected=150),
            TestCase(input=read_file("day02"), expected=1989265)
        ]

        for case in testcases:
            actual = calculate_position(case.input)
            self.assertEqual(case.expected, actual)

    def test_calculate_aim(self):
        testcases = [
            TestCase(input=["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"], expected=900),
            TestCase(input=read_file("day02"), expected=1989265)
        ]

        for case in testcases:
            actual = calculate_aim(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
