import textwrap
import unittest
from dataclasses import dataclass
from typing import List

from day09.smoke_basin import sum_low_point_risk_level, read_file, multiply_largest_basins


@dataclass
class TestCase:
    input: str
    expected: int


class TestSmokeBasin(unittest.TestCase):
    def test_count_simple_digits(self):
        testcases = [
            TestCase(input=textwrap.dedent(
                """
                2199943210
                3987894921
                9856789892
                8767896789
                9899965678
                """).strip()
                     , expected=15),
            TestCase(input=read_file(), expected=524)
        ]
        for case in testcases:
            actual = sum_low_point_risk_level(case.input)
            self.assertEqual(case.expected, actual)

    def test_multiply_largest_basins(self):
        testcases = [
            TestCase(input=textwrap.dedent(
                """
                2199943210
                3987894921
                9856789892
                8767896789
                9899965678
                """).strip()
                     , expected=1134),
            TestCase(input=read_file(), expected=1235430)
        ]
        for case in testcases:
            actual = multiply_largest_basins(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
