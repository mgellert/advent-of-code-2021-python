import math
from typing import Tuple, Type, List


def parse(raw: str) -> List[any]:
    a = []
    a.append(eval(raw))
    return a


def _search_and_add_right(number: List[any], exploded_node, value_to_add, depth=0):
    if type(number) is int:
        return False
    right = number[1]
    if type(right) is int:
        number[1] += value_to_add
        return True
    elif type(right) is list and right != exploded_node:
        return _search_and_add_right(number[0], exploded_node, value_to_add, depth + 1)


def _search_and_add_left(number: List[any], exploded_node, value_to_add):
    if type(number) is int:
        return False
    left = number[0]
    if type(left) is int:
        number[0] += value_to_add
        return True
    elif type(left) is list and left != exploded_node:
        return _search_and_add_left(left, exploded_node, value_to_add)


def explode(number: List[any], depth: int = 0, exploded_once: bool = False):
    left, right, exploded_node = None, None, None
    for i in number:
        if depth == 3 and type(i) is list and not exploded_once:
            if type(i[0]) is list:
                left, right = i[0]
                i[0] = 0
                i[1] += right
                return left, None, i, True
            if type(i[1]) is list:
                left, right = i[1]
                i[1] = 0
                i[0] += left
                return None, right, i, True

        if type(i) is not int and not exploded_node:
            left, right, exploded_node, exploded_once = explode(i, depth + 1, exploded_once)
        if right is not None:
            added = _search_and_add_right(i, exploded_node, right)
            if added:
                return None, None, None, exploded_once
        if left is not None:
            added = _search_and_add_left(i, exploded_node, left)
            if added:
                return None, None, None, exploded_once
    return left, right, exploded_node, exploded_once


def reduce(raw: str):
    number = parse(raw)
    explode(number)
