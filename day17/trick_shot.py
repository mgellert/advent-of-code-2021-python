from typing import Tuple


class Probe:
    x: int
    y: int
    vx: int
    vy: int

    def __init__(self, vx: int, vy: int):
        self.vx = vx
        self.vy = vy
        self.x = 0
        self.y = 0


def _is_probe_within_target(probe: Probe, x: Tuple[int, int], y: Tuple[int, int]):
    return x[0] <= probe.x <= x[1] and y[0] >= probe.y >= y[1]


def hits_target(probe: Probe, x: Tuple[int, int], y: Tuple[int, int]) -> (bool, int):
    highest_y = 0
    while probe.x < x[1] and probe.y > y[1]:
        probe.x += probe.vx
        probe.y += probe.vy
        highest_y = max(highest_y, probe.y)
        if probe.vx > 0:
            probe.vx -= 1
        elif probe.vx < 0:
            probe.vx += 1
        probe.vy -= 1

        if _is_probe_within_target(probe, x, y):
            return True, highest_y
    return False, 0


def find_highest_y(x: Tuple[int, int], y: Tuple[int, int]) -> int:
    highest_y_values = []
    for vx in range(0, 1000):
        for vy in range(0, 1000):
            probe = Probe(vx, vy)
            hits, highest_y = hits_target(probe, x, y)
            if hits:
                highest_y_values.append(highest_y)
    return max(highest_y_values)


def count_all_hits(x: Tuple[int, int], y: Tuple[int, int]) -> int:
    count = 0
    for vx in range(0, 1000):
        for vy in range(-1000, 1000):
            probe = Probe(vx, vy)
            hits, _ = hits_target(probe, x, y)
            if hits:
                count += 1
    return count
