import unittest

from common import read_lines
from day20.trench_map import parse, add_border, DARK_PX, enhance, count_light, apply_enhancement


class BeaconScannerTest(unittest.TestCase):
    test_input = read_lines("day20_test")
    input = read_lines("day20")

    def test_parse(self):
        algorithm, image = parse(self.test_input)
        self.assertEqual(len(algorithm), 512)
        self.assertEqual(len(image), 5)
        self.assertEqual(len(image[0]), 5)

    def test_add_border(self):
        algorithm, image = parse(self.test_input)
        add_border(image, DARK_PX)
        self.assertEqual(len(image), 7)
        self.assertEqual(len(image[0]), 7)

    def test_enhance(self):
        algorithm, image = parse(self.test_input)
        new_image = enhance(algorithm, add_border(image, DARK_PX), DARK_PX)
        new_image = enhance(algorithm, add_border(new_image, DARK_PX), DARK_PX)
        self.assertEqual(count_light(new_image), 35)

    def test_solve_part_1(self):
        algorithm, image = parse(self.input)
        result = apply_enhancement(algorithm, image, 2)
        self.assertEqual(result, 5432)

    def test_solve_part_2(self):
        algorithm, image = parse(self.input)
        result = apply_enhancement(algorithm, image, 50)
        self.assertEqual(result, 16016)