import unittest

from common import read_lines
from day10.syntax_scoring import part_1, part_2


class SyntaxScoringTest(unittest.TestCase):
    test_input = [
        "[({(<(())[]>[[{[]{<()<>>",
        "[(()[<>])]({[<{<<[]>>(",
        "{([(<{}[<>[]}>{[]{[(<()>",
        "(((({<>}<{<{<>}{[]{[]{}",
        "[[<[([]))<([[{}[[()]]]",
        "[{[{({}]{}}([{[{{{}}([]",
        "{<[[]]>}<{[{[{[]{()[[[]",
        "[<(<(<(<{}))><([]([]()",
        "<{([([[(<>()){}]>(<<{{",
        "<{([{{}}[<[[[<>{}]]]>[]]"
    ]
    input = read_lines("day10")

    def test_part_1_example(self):
        self.assertEqual(part_1(self.test_input), 26397)

    def test_part_1_solution(self):
        self.assertEqual(part_1(self.input), 166191)

    def test_part_2_example(self):
        self.assertEqual(part_2(self.test_input), 288957)

    def test_part_2_solution(self):
        self.assertEqual(part_2(self.input), 1152088313)


if __name__ == '__main__':
    unittest.main()
