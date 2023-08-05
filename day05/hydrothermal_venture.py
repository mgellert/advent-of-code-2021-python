import math
import re
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple, Dict, Sequence

line_re = re.compile("(\\d+),(\\d+) -> (\\d+),(\\d+)")


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int

    def calculate_delta(self, other: "Point") -> (int, int):
        return sign(other.x - self.x), sign(other.y - self.y)

    def is_diagonal(self, other: "Point") -> bool:
        dx, dy = self.calculate_delta(other)
        return dx != 0 and dy != 0


def parse_lines(lines: Sequence[str]) -> List[Tuple[Point, Point]]:
    points = []
    for line in lines:
        m = line_re.match(line)
        p1 = Point(x=int(m.group(1)), y=int(m.group(2)))
        p2 = Point(x=int(m.group(3)), y=int(m.group(4)))
        points.append((p1, p2))
    return points


def _add_intermediate_points(diagram: Dict[Point, int], p1: Point, p2: Point):
    dx, dy = p1.calculate_delta(p2)
    i = p1
    while i != p2:
        diagram[i] += 1
        i = Point(i.x + dx, i.y + dy)
    diagram[i] += 1


def _build_diagram(points: List[Tuple[Point, Point]], use_diagonals: bool) -> Dict[Point, int]:
    diagram: Dict[Point, int] = defaultdict(int)
    for point in points:
        p1, p2 = point
        if not use_diagonals and p1.is_diagonal(p2):
            continue
        _add_intermediate_points(diagram, p1, p2)
    return diagram


def sign(n: int) -> int:
    return (n > 0) - (n < 0)


def count_dangerous_areas(points: List[Tuple[Point, Point]], use_diagonals: bool = False) -> int:
    diagram = _build_diagram(points, use_diagonals)
    return sum(1 for _, danger in diagram.items() if danger > 1)
