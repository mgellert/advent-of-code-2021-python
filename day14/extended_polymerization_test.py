import unittest

from common import read_lines
from day14.extended_polymerization import most_and_least_common


class ExtendedPolymerizationTest(unittest.TestCase):
    test_input = [
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
    ]
    input = read_lines("day14")

    def test_part_1_example(self):
        self.assertEqual(most_and_least_common(self.test_input, steps=10), 1588)

    def test_part_1_solution(self):
        self.assertEqual(most_and_least_common(self.input, steps=10), 3284)

    def test_part_2_example(self):
        self.assertEqual(most_and_least_common(self.test_input, steps=40), 2188189693529)

    def test_part_2_solution(self):
        self.assertEqual(most_and_least_common(self.input, steps=40), 4302675529689)


if __name__ == '__main__':
    unittest.main()
