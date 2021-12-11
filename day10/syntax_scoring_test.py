import unittest
from dataclasses import dataclass
from typing import List

from day10.syntax_scoring import calculate_syntax_error_score, read_file, calculate_autocomplete_score


@dataclass
class TestCase:
    input: List[str]
    expected: int


class SyntaxScoringTest(unittest.TestCase):
    def test_calculate_syntax_error_score(self):
        testcases = [
            TestCase(input=[
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
            ], expected=26397),
            TestCase(input=read_file(), expected=166191),
        ]
        for case in testcases:
            actual = calculate_syntax_error_score(case.input)
            self.assertEqual(case.expected, actual)

    def test_calculate_autocomplete_score(self):
        testcases = [
            TestCase(input=[
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
            ], expected=288957),
            TestCase(input=read_file(), expected=1),
        ]
        for case in testcases:
            actual = calculate_autocomplete_score(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
