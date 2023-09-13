import re
from dataclasses import dataclass
from typing import List, Tuple, Set, Type

dot_re = re.compile("(\\d+),(\\d+)")
fold_re = re.compile("fold along ([xy])=(\\d+)")


@dataclass(frozen=True)
class Dot:
    x: int
    y: int

    def __lt__(self, other: Type["Dot"]):
        if self.y != other.y:
            return self.y < other.y
        else:
            return self.x < other.x


@dataclass(frozen=True)
class Fold:
    direction: str
    position: int


def _parse_dots(lines: List[str]) -> Set[Dot]:
    dots = set()
    for line in lines:
        m = dot_re.match(line)
        if m:
            dots.add(Dot(x=int(m[1]), y=int(m[2])))
    return dots


def _parse_folds(lines: List[str]) -> List[Fold]:
    folds = []
    for line in lines:
        m = fold_re.match(line)
        if m:
            folds.append(Fold(m[1], int(m[2])))
    return folds


def _fold(dots: Set[Dot], fold: Fold) -> Set[Dot]:
    folded = set()
    if fold.direction == 'y':
        for dot in dots:
            if dot.y < fold.position:
                folded.add(dot)
            elif dot.y > fold.position:
                folded.add(Dot(y=2 * fold.position - dot.y, x=dot.x))
    elif fold.direction == 'x':
        for dot in dots:
            if dot.x < fold.position:
                folded.add(dot)
            elif dot.x > fold.position:
                folded.add(Dot(x=2 * fold.position - dot.x, y=dot.y))
    return folded


def _print(dots: Set[Dot]) -> str:
    max_x = max(d.x for d in dots)
    max_y = max(d.y for d in dots)

    paper = ""
    for i in range(0, max_y + 1):
        for j in range(0, max_x + 1):
            char = "#" if Dot(y=i, x=j) in dots else " "
            paper += char
        paper += "\n"
    return paper


def visible_dots_after_first_fold(lines: List[str]) -> int:
    dots = _parse_dots(lines)
    folds = _parse_folds(lines)

    folded = _fold(dots, folds[0])
    return len(folded)


def fold_all(lines: List[str]) -> str:
    dots = _parse_dots(lines)
    folds = _parse_folds(lines)

    for fold in folds:
        dots = _fold(dots, fold)
    return _print(dots)
