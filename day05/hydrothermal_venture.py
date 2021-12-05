import re
from dataclasses import dataclass
from typing import List, Tuple, Dict


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


line_re = re.compile("(\\d+),(\\d+) -> (\\d+),(\\d+)")


def _parse_lines(lines: List[str]) -> List[Tuple[Point, Point]]:
    points = []
    for line in lines:
        m = line_re.match(line)
        p1 = Point(x=int(m.group(1)), y=int(m.group(2)))
        p2 = Point(x=int(m.group(3)), y=int(m.group(4)))
        points.append((p1, p2))
    return points


def _add_or_default(map: Dict[Point, int], point: Point):
    if point in map:
        map[point] = map[point] + 1
    else:
        map[point] = 1


def _calculate_delta(p1: Point, p2: Point) -> Point:
    return Point(sign(p2.x - p1.x), sign(p2.y - p1.y))


def _build_map(points: List[Tuple[Point, Point]], diagonal: bool) -> Dict[Point, int]:
    map = {}
    for point in points:
        p1, p2 = point
        dp = _calculate_delta(p1, p2)
        if not diagonal and dp.x != 0 and dp.y != 0:
            continue
        curr = p1
        while curr != p2:
            _add_or_default(map, curr)
            curr = Point(curr.x + dp.x, curr.y + dp.y)
        _add_or_default(map, curr)
    return map


def read_file() -> List[str]:
    with open("../inputs/day05", "r") as file:
        return file.readlines()


def sign(a: int) -> int:
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0


def count_dangerous_areas(lines: List[str], diagonal: bool = False) -> int:
    points = _parse_lines(lines)
    map = _build_map(points, diagonal)
    return len([1 for _, danger in map.items() if danger > 1])
