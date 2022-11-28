import unittest

from day18.snailfish import parse, explode


class SnailfishTest(unittest.TestCase):
    def test_explode(self):
        # actual = parse("[[[[[9,8],1],2],3],4]")
        # expected = parse("[[[[0,9],2],3],4]")
        # explode(actual)
        # self.assertEqual(expected, actual)
        #
        # actual = parse("[7,[6,[5,[4,[3,2]]]]]")
        # expected = parse("[7,[6,[5,[7,0]]]]")
        # explode(actual)
        # self.assertEqual(expected, actual)
        #
        # actual = parse("[[6,[5,[4,[3,2]]]],1]")
        # expected = parse("[[6,[5,[7,0]]],3]")
        # explode(actual)
        # self.assertEqual(expected, actual)

        actual = parse("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        expected = parse("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        explode(actual)
        self.assertEqual(expected, actual)
        #
        # actual = parse("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        # expected = parse("[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
        # explode(actual)
        # self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
