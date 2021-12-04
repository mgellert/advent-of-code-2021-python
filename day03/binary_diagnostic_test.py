import unittest
from dataclasses import dataclass
from typing import List

from day03.binary_diagnostic import calculate_power_consumption, read_file, find_life_support_rating


@dataclass
class TestCase:
    input: List[str]
    expected: int


class BinaryDiagnosticTest(unittest.TestCase):
    def test_calculate_power_consumption(self):
        testcases = [
            TestCase(input=["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                            "00010", "01010", ], expected=198),
            TestCase(input=read_file("day03"), expected=3847100)
        ]

        for case in testcases:
            actual = calculate_power_consumption(case.input)
            self.assertEqual(case.expected, actual)

    def test_find_life_support_rating(self):
        testcases = [
            TestCase(input=["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001",
                            "00010", "01010", ], expected=230),
            TestCase(input=read_file("day03"), expected=4105235)
        ]

        for case in testcases:
            actual = find_life_support_rating(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
