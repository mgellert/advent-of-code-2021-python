import unittest
from dataclasses import dataclass
from typing import List, Callable

from day07.treachery_of_whale import read_file, find_optimal_pos, constant, \
    increasing


@dataclass
class TestCase:
    input: List[int]
    fuel_consumption: Callable[[int, int], int]
    expected: int


class TreacheryOfWhaleTest(unittest.TestCase):
    def test_find_optimal_pos(self):
        testcases = [
            TestCase(input=[16, 1, 2, 0, 4, 2, 7, 1, 2, 14], fuel_consumption=constant, expected=37),
            TestCase(input=read_file(), fuel_consumption=constant, expected=328318),
            TestCase(input=[16, 1, 2, 0, 4, 2, 7, 1, 2, 14], fuel_consumption=increasing, expected=168),
            TestCase(input=read_file(), fuel_consumption=increasing, expected=89791146),
        ]

        for case in testcases:
            actual = find_optimal_pos(case.input, case.fuel_consumption)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
