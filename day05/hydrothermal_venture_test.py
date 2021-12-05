import unittest
from dataclasses import dataclass
from typing import List

from day05.hydrothermal_venture import count_dangerous_areas, read_file


@dataclass
class TestCase:
    input: List[str]
    expected: int


class HydrothermalVentureTest(unittest.TestCase):
    def test_count_dangerous_areas(self):
        testcases = [
            TestCase(input=[
                "0,9 -> 5,9",
                "8,0 -> 0,8",
                "9,4 -> 3,4",
                "2,2 -> 2,1",
                "7,0 -> 7,4",
                "6,4 -> 2,0",
                "0,9 -> 2,9",
                "3,4 -> 1,4",
                "0,0 -> 8,8",
                "5,5 -> 8,2"
            ], expected=5),
            TestCase(input=read_file(), expected=4826)
        ]
        for case in testcases:
            actual = count_dangerous_areas(case.input)
            self.assertEqual(case.expected, actual)

    def test_count_dangerous_areas_with_diagonal(self):
        testcases = [
            TestCase(input=[
                "0,9 -> 5,9",
                "8,0 -> 0,8",
                "9,4 -> 3,4",
                "2,2 -> 2,1",
                "7,0 -> 7,4",
                "6,4 -> 2,0",
                "0,9 -> 2,9",
                "3,4 -> 1,4",
                "0,0 -> 8,8",
                "5,5 -> 8,2"
            ], expected=12),
            TestCase(input=read_file(), expected=16793)
        ]
        for case in testcases:
            actual = count_dangerous_areas(case.input, diagonal=True)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
