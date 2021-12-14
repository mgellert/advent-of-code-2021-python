import unittest
from dataclasses import dataclass
from typing import List

from day14.extended_polymerization import most_and_least_common, read_input


@dataclass
class TestCase:
    input: List[str]
    expected: int


class ExtendedPolymerizationTest(unittest.TestCase):
    def test_visible_dots_after_first_fold_10_steps(self):
        testcases = [
            TestCase(input=[
                "NNCB",
                "",
                "CH -> B",
                "HH -> N",
                "CB -> H",
                "NH -> C",
                "HB -> C",
                "HC -> B",
                "HN -> C",
                "NN -> C",
                "BH -> H",
                "NC -> B",
                "NB -> B",
                "BN -> B",
                "BB -> N",
                "BC -> B",
                "CC -> N",
                "CN -> C"
            ], expected=1588),
            TestCase(input=read_input(), expected=3284)
        ]

        for case in testcases:
            actual = most_and_least_common(case.input)
            self.assertEqual(case.expected, actual)

    def test_visible_dots_after_first_fold_40_steps(self):
        testcases = [
            TestCase(input=[
                "NNCB",
                "",
                "CH -> B",
                "HH -> N",
                "CB -> H",
                "NH -> C",
                "HB -> C",
                "HC -> B",
                "HN -> C",
                "NN -> C",
                "BH -> H",
                "NC -> B",
                "NB -> B",
                "BN -> B",
                "BB -> N",
                "BC -> B",
                "CC -> N",
                "CN -> C"
            ], expected=2188189693529),
            TestCase(input=read_input(), expected=4302675529689)
        ]

        for case in testcases:
            actual = most_and_least_common(case.input, steps=40)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
