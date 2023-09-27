import unittest

from common import read_lines
from day19.beacon_scanner import parse, find_overlaps, find_position, Beacon, solve


class BeaconScannerTest(unittest.TestCase):
    test_input = read_lines("day19_test")
    input = read_lines("day19")

    def test_parse(self):
        scanners = parse(self.test_input)
        self.assertEqual("scanner 0", scanners[0].name)
        self.assertEqual(Beacon(404, -588, -901), scanners[0].beacons[0])
        self.assertEqual("scanner 4", scanners[4].name)

    def test_1(self):
        scanners = parse(self.test_input)
        overlaps = find_overlaps(scanners[0], scanners[1])
        self.assertEqual(11, len(overlaps))
        all_beacons = find_position(scanners[0], scanners[1], overlaps)
        self.assertIsNotNone(all_beacons)

    def test_2(self):
        scanners = parse(self.test_input)
        overlaps = find_overlaps(scanners[0], scanners[2])
        self.assertIsNone(overlaps)

    def test_3(self):
        scanners = parse(self.test_input)
        overlaps = find_overlaps(scanners[1], scanners[4])
        self.assertEqual(11, len(overlaps))
        all_beacons = find_position(scanners[1], scanners[4], overlaps)
        self.assertIsNotNone(all_beacons)

    def test_4(self):
        scanners = parse(self.test_input)
        overlaps = find_overlaps(scanners[1], scanners[3])
        self.assertEqual(11, len(overlaps))
        all_beacons = find_position(scanners[1], scanners[3], overlaps)
        self.assertIsNotNone(all_beacons)

    def test_5(self):
        scanners = parse(self.test_input)
        count, max_dist = solve(scanners)
        self.assertEqual(79, count)
        self.assertEqual(3621, max_dist)

    def test_6(self):
        scanners = parse(self.input)
        count, max_dist = solve(scanners)
        self.assertEqual(357, count)
        self.assertEqual(12317, max_dist)


if __name__ == '__main__':
    unittest.main()
