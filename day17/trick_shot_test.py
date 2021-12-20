import unittest
from dataclasses import dataclass
from typing import Tuple

from day17.trick_shot import hits_target, Probe, find_highest_y, count_all_hits


class TrickShotTest(unittest.TestCase):
    def test_probe_hits_target(self):
        @dataclass
        class ProbeHitsTargetTestCase:
            initial_velocity: Tuple[int, int]
            expected_hit: bool
            expected_highest_y: int

        testcases = [
            ProbeHitsTargetTestCase(initial_velocity=(7, 2), expected_hit=True, expected_highest_y=3),
            ProbeHitsTargetTestCase(initial_velocity=(6, 3), expected_hit=True, expected_highest_y=6),
            ProbeHitsTargetTestCase(initial_velocity=(9, 0), expected_hit=True, expected_highest_y=0),
            ProbeHitsTargetTestCase(initial_velocity=(6, 9), expected_hit=True, expected_highest_y=45),
            ProbeHitsTargetTestCase(initial_velocity=(17, -4), expected_hit=False, expected_highest_y=0),
        ]

        for case in testcases:
            hit, highest_y = hits_target(Probe(vx=case.initial_velocity[0], vy=case.initial_velocity[1]), (20, 30),
                                         (-5, -10))
            self.assertEqual(case.expected_hit, hit)
            self.assertEqual(case.expected_highest_y, highest_y)

    def test_find_highest_y(self):
        @dataclass
        class ProbeHitsTargetTestCase:
            x: Tuple[int, int]
            y: Tuple[int, int]
            expected: int

        testcases = [
            ProbeHitsTargetTestCase(x=(20, 30), y=(-5, -10), expected=45),
            ProbeHitsTargetTestCase(x=(32, 65), y=(-177, -225), expected=25200),
        ]

        for case in testcases:
            actual = find_highest_y(x=case.x, y=case.y)
            self.assertEqual(case.expected, actual)

    def test_count_all_hits(self):
        @dataclass
        class ProbeHitsTargetTestCase:
            x: Tuple[int, int]
            y: Tuple[int, int]
            expected: int

        testcases = [
            ProbeHitsTargetTestCase(x=(20, 30), y=(-5, -10), expected=112),
            ProbeHitsTargetTestCase(x=(32, 65), y=(-177, -225), expected=3012),
        ]

        for case in testcases:
            actual = count_all_hits(x=case.x, y=case.y)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
