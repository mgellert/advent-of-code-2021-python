import unittest

from common import read_lines
from day08.seven_segment_search import part_1, part_2, parse_line


class SevenSegmentSearchTest(unittest.TestCase):
    test_input = [parse_line(line) for line in (
        "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
        "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
        "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
        "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
        "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
        "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
        "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
        "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
        "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
        "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
    )]
    input = [parse_line(line) for line in read_lines("day08")]

    def test_part_1_example(self):
        self.assertEqual(part_1(self.test_input), 26)

    def test_part_1_solution(self):
        self.assertEqual(part_1(self.input), 381)

    def test_part_2_example(self):
        self.assertEqual(part_2(self.test_input), 61229)

    def test_part_2_solution(self):
        self.assertEqual(part_2(self.input), 1023686)


if __name__ == '__main__':
    unittest.main()
