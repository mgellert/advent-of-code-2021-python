import unittest
from dataclasses import dataclass
from typing import List

from day12.passage_pathing import count_paths, read_file, count_paths2


@dataclass
class TestCase:
    input: List[str]
    expected: int


class PassagePathingTest(unittest.TestCase):
    def test_count_paths(self):
        testcases = [
            TestCase(input=[
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ], expected=10),
            TestCase(input=read_file(), expected=1)
        ]

        for case in testcases:
            actual = count_paths(case.input)
            self.assertEqual(case.expected, actual)

    def test_count_paths2(self):
        testcases = [
            TestCase(input=[
                "start-A",
                "start-b",
                "A-c",
                "A-b",
                "b-d",
                "A-end",
                "b-end",
            ], expected=36),
            TestCase(input=read_file(), expected=144309)
        ]

        for case in testcases:
            actual = count_paths2(case.input)
            self.assertEqual(case.expected, actual)
if __name__ == '__main__':
    unittest.main()
