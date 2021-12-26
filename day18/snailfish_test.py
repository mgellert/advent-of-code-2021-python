import unittest

from day18.snailfish import explode, Node, parse, split, reduce


class SnailfishTest(unittest.TestCase):
    def test_parsing(self):
        actual = parse("[1,2]")
        expected = Node(left=1, right=2)
        self.assertEqual(expected, actual)

        actual = parse("[3,[1,2]]")
        expected = Node(left=3, right=Node(left=1, right=2))
        self.assertEqual(expected, actual)

    def test_explode(self):
        actual = parse("[[[[[9,8],1],2],3],4]")
        expected = parse("[[[[0,9],2],3],4]")
        explode(actual)
        self.assertEqual(expected, actual)

        actual = parse("[7,[6,[5,[4,[3,2]]]]]")
        expected = parse("[7,[6,[5,[7,0]]]]")
        explode(actual)
        self.assertEqual(expected, actual)

        actual = parse("[[6,[5,[4,[3,2]]]],1]")
        expected = parse("[[6,[5,[7,0]]],3]")
        explode(actual)
        self.assertEqual(expected, actual)

        actual = parse("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
        expected = parse("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        explode(actual)
        self.assertEqual(expected, actual)

        actual = parse("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")
        expected = parse("[[3,[2,[8,0]]],[9,[5,[7,0]]]]")
        explode(actual)
        self.assertEqual(expected, actual)

    def test_split(self):
        actual = parse("[1,10]")
        expected = parse("[1,[5,5]]")
        splitted = split(actual)
        self.assertEqual(expected, actual)
        self.assertTrue(splitted)

        actual = parse("[1,11]")
        expected = parse("[1,[5,6]]")
        splitted = split(actual)
        self.assertEqual(expected, actual)
        self.assertTrue(splitted)

        actual = parse("[10,10]")
        expected = parse("[[5,5],10]")
        splitted = split(actual)
        self.assertEqual(expected, actual)
        self.assertTrue(splitted)

        actual = parse("[1,1]")
        expected = parse("[1,1]")
        splitted = split(actual)
        self.assertEqual(expected, actual)
        self.assertFalse(splitted)

    def test_reduce(self):
        actual = parse("[[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]]")
        expected = parse("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
        reduce(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
