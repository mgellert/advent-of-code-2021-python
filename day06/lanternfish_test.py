import unittest
from dataclasses import dataclass
from typing import List

from day06.lanternfish import count_fish_after_days, read_file


@dataclass
class TestCase:
    input: List[int]
    days: int
    expected: int


class LanternfishTest(unittest.TestCase):
    def test_count_fish_after_days(self):
        testcases = [
            TestCase(input=[3, 4, 3, 1, 2], days=80, expected=5934),
            TestCase(input=read_file(), days=80, expected=380243),
            TestCase(input=[3, 4, 3, 1, 2], days=256, expected=26984457539),
            TestCase(input=read_file(), days=256, expected=1708791884591),
        ]
        for case in testcases:
            actual = count_fish_after_days(case.days, case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
