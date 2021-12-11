from functools import reduce
from typing import List, Set, Tuple


def read_file() -> str:
    with open("../inputs/day09", "r") as file:
        return file.read()


def _parse_input(input: str) -> List[List[int]]:
    return [[int(c) for c in line] for line in input.split("\n")]


def _is_lowpoint(i: int, j: int, map: List[List[int]]) -> bool:
    top = map[i - 1][j] if i > 0 else 99
    right = map[i][j + 1] if j < len(map[i]) - 1 else 99
    bottom = map[i + 1][j] if i < len(map) - 1 else 99
    left = map[i][j - 1] if j > 0 else 99
    middle = map[i][j]
    return middle < top and middle < right and middle < bottom and middle < left


def _count_basin(i: int, j: int, map: List[List[int]]) -> int:
    basin: Set[Tuple[int, int]] = set()
    basin.add((i, j))
    prev_len = 0

    while prev_len < len(basin):
        new_points: Set[Tuple[int, int]] = set()
        for p in basin:
            i = p[0]
            j = p[1]
            top = map[i - 1][j] if i > 0 else 9
            right = map[i][j + 1] if j < len(map[i]) - 1 else 9
            bottom = map[i + 1][j] if i < len(map) - 1 else 9
            left = map[i][j - 1] if j > 0 else 9

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


def sum_low_point_risk_level(input: str) -> int:
    map = _parse_input(input)
    sum = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if _is_lowpoint(i, j, map):
                sum += 1 + map[i][j]
    return sum


def multiply_largest_basins(input: str) -> int:
    map = _parse_input(input)
    basins: List[int] = []
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if _is_lowpoint(i, j, map):
                basins.append(_count_basin(i, j, map))

    return reduce(lambda x, y: x * y, list(reversed(sorted(basins)))[0:3])
