from functools import reduce
from typing import List, Set, Tuple

Heightmap = List[List[int]]
Point = Tuple[int, int]


def parse_input(raw: str) -> Heightmap:
    return [[int(c) for c in line] for line in raw.split("\n")]


def _is_low_point(i: int, j: int, heightmap: Heightmap) -> bool:
    top = heightmap[i - 1][j] if i > 0 else 9
    right = heightmap[i][j + 1] if j < len(heightmap[i]) - 1 else 9
    bottom = heightmap[i + 1][j] if i < len(heightmap) - 1 else 9
    left = heightmap[i][j - 1] if j > 0 else 9
    middle = heightmap[i][j]
    return middle < top and middle < right and middle < bottom and middle < left


def _count_basin(i: int, j: int, heightmap: Heightmap) -> int:
    basin: Set[Point] = set()
    basin.add((i, j))
    prev_len = 0

    while prev_len < len(basin):
        new_points: Set[Point] = set()
        for p in basin:
            i, j = p
            top = heightmap[i - 1][j] if i > 0 else 9
            right = heightmap[i][j + 1] if j < len(heightmap[i]) - 1 else 9
            bottom = heightmap[i + 1][j] if i < len(heightmap) - 1 else 9
            left = heightmap[i][j - 1] if j > 0 else 9

            if top < 9:
                new_points.add((i - 1, j))
            if right < 9:
                new_points.add((i, j + 1))
            if bottom < 9:
                new_points.add((i + 1, j))
            if left < 9:
                new_points.add((i, j - 1))

        prev_len = len(basin)
        basin = basin.union(new_points)

    return len(basin)


def part_1(heightmap: Heightmap) -> int:
    sum_risk = 0
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[i])):
            if _is_low_point(i, j, heightmap):
                sum_risk += 1 + heightmap[i][j]
    return sum_risk


def part_2(heightmap: Heightmap) -> int:
    basins: List[int] = []
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[i])):
            if _is_low_point(i, j, heightmap):
                basins.append(_count_basin(i, j, heightmap))

    return reduce(lambda x, y: x * y, list(reversed(sorted(basins)))[0:3])
