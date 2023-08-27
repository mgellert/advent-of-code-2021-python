import unittest

from common import read_lines
from day12.passage_pathing import count_paths, count_paths2, parse_input


class PassagePathingTest(unittest.TestCase):
    test_input = parse_input([
        "start-A",
        "start-b",
        "A-c",
        "A-b",
        "b-d",
        "A-end",
        "b-end",
    ])
    input = parse_input(read_lines("day12"))

    def test_part_1_example(self):
        self.assertEqual(count_paths(self.test_input), 10)

    def test_part_1_solution(self):
        self.assertEqual(count_paths(self.input), 5157)

    def test_part_2_example(self):
        self.assertEqual(count_paths2(self.test_input), 36)

    def test_part_2_solution(self):
        self.assertEqual(count_paths2(self.input), 144309)


if __name__ == '__main__':
    unittest.main()
