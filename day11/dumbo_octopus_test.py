import textwrap
import unittest
from dataclasses import dataclass

from day11.dumbo_octopus import count_flashes, read_file, count_sync


@dataclass
class TestCase:
    input: str
    expected: int


class DumboOctopusTest(unittest.TestCase):
    def test_count_flashes(self):
        testcases = [
            TestCase(input=textwrap.dedent("""
            5483143223
            2745854711
            5264556173
            6141336146
            6357385478
            4167524645
            2176841721
            6882881134
            4846848554
            5283751526
            """).strip(), expected=1656),
            TestCase(input=read_file(), expected=1749)
        ]
        for case in testcases:
            actual = count_flashes(case.input)
            self.assertEqual(case.expected, actual)

    def test_count_sync(self):
        testcases = [
            TestCase(input=textwrap.dedent("""
            5483143223
            2745854711
            5264556173
            6141336146
            6357385478
            4167524645
            2176841721
            6882881134
            4846848554
            5283751526
            """).strip(), expected=195),
            TestCase(input=read_file(), expected=285)
        ]
        for case in testcases:
            actual = count_sync(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
