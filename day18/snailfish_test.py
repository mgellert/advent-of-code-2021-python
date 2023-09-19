import unittest

from common import read_lines
from day18.snailfish import parse, add, explode, wrap, unwrap, split, magnitude, reduce, calc_sum, calc_max_sum


class SnailfishTest(unittest.TestCase):

    def test_parse(self):
        self.assertEqual(parse("[1,2]"), [1, 2])
        self.assertEqual([[1, 2], [[3, 4], 5]], parse("[[1,2],[[3,4],5]]"))

    def test_add(self):
        result = add([1, 2], [[3, 4], 5])
        self.assertEqual([[1, 2], [[3, 4], 5]], result)

    def test_wrap(self):
        result = wrap([[3, 4], 5])
        self.assertEqual("[[3, 4], 5]", str(result))

    def test_explode_1(self):
        number = wrap([[[[[9, 8], 1], 2], 3], 4])
        result = unwrap(explode(number))
        self.assertEqual([[[[0, 9], 2], 3], 4], result)

    def test_explode_2(self):
        number = wrap([7, [6, [5, [4, [3, 2]]]]])
        result = unwrap(explode(number))
        self.assertEqual([7, [6, [5, [7, 0]]]], result)

    def test_explode_3(self):
        number = wrap([[6, [5, [4, [3, 2]]]], 1])
        result = unwrap(explode(number))
        self.assertEqual([[6, [5, [7, 0]]], 3], result)

    def test_explode_4(self):
        number = wrap([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
        result = unwrap(explode(number))
        self.assertEqual([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]], result)

    def test_explode_5(self):
        number = wrap([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
        result = unwrap(explode(number))
        self.assertEqual([[3, [2, [8, 0]]], [9, [5, [7, 0]]]], result)

    def test_explode_6(self):
        number = wrap([1, 2])
        result = unwrap(explode(number))
        self.assertIsNone(result)

    def test_split_1(self):
        number = wrap([10, 2])
        result = unwrap(split(number))
        self.assertEqual([[5, 5], 2], result)

    def test_split_2(self):
        number = wrap([11, 2])
        result = unwrap(split(number))
        self.assertEqual([[5, 6], 2], result)

    def test_reduce_manually(self):
        # add
        number = add(wrap([[[[4, 3], 4], 4], [7, [[8, 4], 9]]]), wrap([1, 1]))
        self.assertEqual([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]], unwrap(number))
        # explode
        number = explode(wrap(number))
        self.assertEqual([[[[0, 7], 4], [7, [[8, 4], 9]]], [1, 1]], unwrap(number))
        # explode
        number = explode(wrap(number))
        self.assertEqual([[[[0, 7], 4], [15, [0, 13]]], [1, 1]], unwrap(number))
        # split
        number = split(wrap(number))
        self.assertEqual([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]], unwrap(number))
        # split
        number = split(wrap(number))
        self.assertEqual([[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]], unwrap(number))
        # explode
        number = explode(wrap(number))
        self.assertEqual([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], unwrap(number))

    def test_magnitude_1(self):
        number = wrap([[9, 1], [1, 9]])
        result = magnitude(number)
        self.assertEqual(129, result)

    def test_magnitude_2(self):
        number = wrap([[1, 2], [[3, 4], 5]])
        result = magnitude(number)
        self.assertEqual(143, result)

    def test_magnitude_3(self):
        number = wrap([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]])
        result = magnitude(number)
        self.assertEqual(1384, result)

    def test_magnitude_4(self):
        number = wrap([[[[1, 1], [2, 2]], [3, 3]], [4, 4]])
        result = magnitude(number)
        self.assertEqual(445, result)

    def test_magnitude_5(self):
        number = wrap([[[[3, 0], [5, 3]], [4, 4]], [5, 5]])
        result = magnitude(number)
        self.assertEqual(791, result)

    def test_magnitude_6(self):
        number = wrap([[[[5, 0], [7, 4]], [5, 5]], [6, 6]])
        result = magnitude(number)
        self.assertEqual(1137, result)

    def test_magnitude_7(self):
        number = wrap([[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]])
        result = magnitude(number)
        self.assertEqual(3488, result)

    def test_reduce(self):
        number = add(wrap([[[[4, 3], 4], 4], [7, [[8, 4], 9]]]), wrap([1, 1]))
        number = reduce(number)
        self.assertEqual([[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]], unwrap(number))

    def test_example_1(self):
        test_input = [
            "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",
            "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",
            "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",
            "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",
            "[7,[5,[[3,8],[1,4]]]]",
            "[[2,[2,2]],[8,[8,1]]]",
            "[2,9]",
            "[1,[[[9,3],9],[[9,0],[0,7]]]]",
            "[[[5,[7,4]],7],1]",
            "[[[[4,2],2],6],[8,7]]"
        ]
        sum = calc_sum(test_input)
        self.assertEqual(3488, sum)

    def test_example_2(self):
        test_input = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        sum = calc_sum(test_input)
        self.assertEqual(4140, sum)

    def test_part_1(self):
        input = read_lines("day18")
        sum = calc_sum(input)
        self.assertEqual(3216, sum)

    def test_example_3(self):
        test_input = [
            "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
            "[[[5,[2,8]],4],[5,[[9,9],0]]]",
            "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
            "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
            "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
            "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
            "[[[[5,4],[7,7]],8],[[8,3],8]]",
            "[[9,3],[[9,9],[6,[4,9]]]]",
            "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
            "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"
        ]
        sum = calc_max_sum(test_input)
        self.assertEqual(3993, sum)

    def test_part_2(self):
        input = read_lines("day18")
        sum = calc_max_sum(input)
        self.assertEqual(4643, sum)


if __name__ == '__main__':
    unittest.main()
