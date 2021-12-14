import re
from dataclasses import dataclass
from typing import List, Tuple, Set, Type

dot_re = re.compile("(\\d+),(\\d+)")
fold_re = re.compile("fold along ([xy])=(\\d+)")


def read_input() -> List[str]:
    with open("../inputs/day13", "r") as file:
        return file.readlines()


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __lt__(self, other: Type["Point"]):
        if self.y != other.y:
            return self.y < other.y
        else:
            return self.x < other.x


def _parse_dots(lines: List[str]) -> Set[Point]:
    dots = set()
    for line in lines:
        m = dot_re.match(line)
        if m:
            dots.add(Point(x=int(m[1]), y=int(m[2])))
    return dots


def _parse_folds(lines: List[str]) -> List[Tuple[str, int]]:
    folds = []
    for line in lines:
        m = fold_re.match(line)
        if m:
            folds.append((m[1], int(m[2])))
    return folds


def _fold(dots: Set[Point], dir: str, pos: int) -> Set[Point]:
    folded = set()
    if dir == 'y':
        for dot in dots:
            if dot.y < pos:
                folded.add(dot)
            elif dot.y > pos:
                folded.add(Point(y=2 * pos - dot.y, x=dot.x))
    elif dir == 'x':
        for dot in dots:
            if dot.x < pos:
                folded.add(dot)
            elif dot.x > pos:
                folded.add(Point(x=2 * pos - dot.x, y=dot.y))
    return folded


def _print(dots: Set[Point]):
    max_x = max([d.x for d in dots])
    max_y = max([d.y for d in dots])

    for i in range(0, max_y + 1):
        for j in range(0, max_x + 1):
            char = "#" if Point(y=i, x=j) in dots else " "
            print(char, end="")
        print()


def visible_dots_after_first_fold(lines: List[str]) -> int:
    dots = _parse_dots(lines)
    folds = _parse_folds(lines)

    folded = _fold(dots, *folds[0])
    return len(folded)


def fold_all(lines: List[str]):
    dots = _parse_dots(lines)
    folds = _parse_folds(lines)

    for fold in folds:
        dots = _fold(dots, *fold)
    _print(dots)
