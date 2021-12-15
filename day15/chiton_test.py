import unittest
from dataclasses import dataclass
from typing import List

from day15.chiton import find_lowest_total_risk_path, read_input, find_lowest_total_risk_path_in_large_area


@dataclass
class TestCase:
    input: List[str]
    expected: int


class ChitonTest(unittest.TestCase):
    def test_find_lowest_total_risk_path(self):
        testcases = [
            TestCase(input=[
                "1163751742",
                "1381373672",
                "2136511328",
                "3694931569",
                "7463417111",
                "1319128137",
                "1359912421",
                "3125421639",
                "1293138521",
                "2311944581"
            ], expected=40),
            TestCase(input=read_input(), expected=390)
        ]

        for case in testcases:
            actual = find_lowest_total_risk_path(case.input)
            self.assertEqual(case.expected, actual)

    def test_find_lowest_total_risk_path_large_area(self):
        testcases = [
            TestCase(input=[
                "1163751742",
                "1381373672",
                "2136511328",
                "3694931569",
                "7463417111",
                "1319128137",
                "1359912421",
                "3125421639",
                "1293138521",
                "2311944581"
            ], expected=315),
            TestCase(input=read_input(), expected=2814)
        ]

        for case in testcases:
            actual = find_lowest_total_risk_path_in_large_area(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
