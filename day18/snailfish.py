import math
from dataclasses import dataclass
from typing import Tuple, Type, List


class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Node):
            return self.left == o.left and self.right == o.right
        return False

    def __str__(self):
        return f"Node(left={self.left}, right={self.right})"

    def __repr__(self) -> str:
        return self.__str__()


def _parse(input) -> Node:
    node = Node()

    if type(input[0]) is int:
        left = input[0]
    else:
        left = _parse(input[0])

    if type(input[1]) is int:
        right = input[1]
    else:
        right = _parse(input[1])

    node.left = left
    node.right = right
    return node


def parse(raw: str) -> Node:
    return _parse(eval(raw))


def _to_list(node, list):
    if type(node) is int:
        return list
    if node.left is not None:
        _to_list(node.left, list)

    if type(node.left) is int or type(node.right) is int:
        list.append(node)

    if node.right is not None:
        _to_list(node.right, list)
    return list


def _add_to_right(list: List[any], value, i):
    if i < len(list):
        node = list[i]
        if type(node.right) is int:
            node.right += value
        elif type(node.left) is int:
            node.left += value


def _add_to_left(list: List[any], value, i):
    if i > 0:
        node = list[i - 1]
        if type(node.left) is int:
            node.left += value
        elif type(node.right) is int:
            node.right += value


def _explode(node, as_list, depth=1, done=False):
    if type(node) is int:
        return None, None, None, None
    if depth == 4 and not done:
        if type(node.left) is Node:
            temp = node.left
            node.left = 0
            return temp.left, temp.right, as_list.index(temp), True
        elif type(node.right) is Node:
            temp = node.right
            node.right = 0
            return temp.left, temp.right, as_list.index(temp), True
    left, right, i, done = _explode(node.left, as_list, depth + 1, done)
    if left is not None and right is not None:
        return left, right, i, done
    left, right, i, done = _explode(node.right, as_list, depth + 1, done)
    if left is not None and right is not None:
        return left, right, i, done

    return None, None, None, None


def explode(node):
    left, right, i, done = _explode(node, _to_list(node, []))
    if not done:
        return False
    _add_to_right(_to_list(node, []), right, i)
    _add_to_left(_to_list(node, []), left, i)
    return True


def split(node, done=False):
    if type(node.left) is int and not done:
        if node.left >= 10:
            value = node.left
            node.left = Node(left=math.floor(value / 2), right=math.ceil(value / 2))
            return True
    if type(node.right) is int and not done:
        if node.right >= 10:
            value = node.right
            node.right = Node(left=math.floor(value / 2), right=math.ceil(value / 2))
            return True
    if type(node.left) is Node:
        done = split(node.left, done)
    if type(node.right) is Node:
        done = split(node.right, done)
    return done


def reduce(node):
    exploded = True
    splitted = True
    while exploded or splitted:
        exploded = explode(node)
        while exploded:
            exploded = explode(node)
            print("exploded")
        splitted = split(node)
        print("splitted")
