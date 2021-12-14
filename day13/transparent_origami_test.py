import unittest
from dataclasses import dataclass
from typing import List

from day13.transparent_origami import visible_dots_after_first_fold, read_input, fold_all


@dataclass
class TestCase:
    input: List[str]
    expected: int


class TransparentOrigamiTest(unittest.TestCase):
    def test_visible_dots_after_first_fold(self):
        testcases = [
            TestCase(input=[
                "6,10",
                "0,14",
                "9,10",
                "0,3",
                "10,4",
                "4,11",
                "6,0",
                "6,12",
                "4,1",
                "0,13",
                "10,12",
                "3,4",
                "3,0",
                "8,4",
                "1,10",
                "2,14",
                "8,10",
                "9,0",
                "",
                "fold along y=7",
                "fold along x=5"
            ], expected=17),
            TestCase(input=read_input(), expected=1)
        ]

        for case in testcases:
            actual = visible_dots_after_first_fold(case.input)
            self.assertEqual(case.expected, actual)

    def test_fold_all(self):
        testcases = [
            TestCase(input=[
                "6,10",
                "0,14",
                "9,10",
                "0,3",
                "10,4",
                "4,11",
                "6,0",
                "6,12",
                "4,1",
                "0,13",
                "10,12",
                "3,4",
                "3,0",
                "8,4",
                "1,10",
                "2,14",
                "8,10",
                "9,0",
                "",
                "fold along y=7",
                "fold along x=5"
            ], expected=17),
            TestCase(input=read_input(), expected=1)
        ]

        for case in testcases:
            fold_all(case.input)


if __name__ == '__main__':
    unittest.main()
