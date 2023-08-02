from typing import List


def part_1(measurements: List[int]) -> int:
    pairs = list(_sliding_window(measurements))
    return sum([1 for a, b in pairs if b > a])


def part_2(measurements: List[int]) -> int:
    triplets = list(_sliding_window(measurements, 3))
    sums = [sum(a) for a in triplets]
    return part_1(sums)


def _sliding_window(seq: List[int], window_size=2) -> List[int]:
    for i in range(len(seq) - window_size + 1):
        yield seq[i: i + window_size]
