import unittest
from dataclasses import dataclass
from typing import List

from day01.sonar_sweep import count_larger_measurements, read_file_to_int, count_larger_sums


class SonarSweepTest(unittest.TestCase):
    def test_count_larger_measurements(self):
        @dataclass
        class TestCase:
            input: List[int]
            expected: int

        testcases = [
            TestCase(input=[199, 200, 208, 210, 200, 207, 240, 269, 260, 263], expected=7),
            TestCase(input=read_file_to_int("day01"), expected=1832)
        ]

        for case in testcases:
            actual = count_larger_measurements(case.input)
            self.assertEqual(case.expected, actual)

    def test_count_larger_sums(self):
        @dataclass
        class TestCase:
            input: List[int]
            expected: int

        testcases = [
            TestCase(input=[199, 200, 208, 210, 200, 207, 240, 269, 260, 263], expected=5),
            TestCase(input=read_file_to_int("day01"), expected=1858)
        ]

        for case in testcases:
            actual = count_larger_sums(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
