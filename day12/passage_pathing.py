import re
from collections import deque
from dataclasses import dataclass
from typing import List, Type, Dict, Set


@dataclass
class Node:
    name: str
    edges: Set[str]

    def is_small(self) -> bool:
        return self.name.islower()


input_re = re.compile("(\\w+)-(\\w+)")


def read_file() -> List[str]:
    with open("../inputs/day12", "r") as file:
        return file.readlines()


def _add_or_create(map: Dict[str, Node], name: str, edge: str):
    if name in map:
        map[name].edges.add(edge)
    else:
        map[name] = Node(name=name, edges=set())
        map[name].edges.add(edge)


def _parse_input(lines: List[str]) -> Dict[str, Node]:
    map = {}
    for line in lines:
        m = input_re.match(line)
        node1 = m[1]
        node2 = m[2]
        _add_or_create(map, node1, node2)
        _add_or_create(map, node2, node1)
    return map


def _bfs(map: Dict[str, Node], current: Node) -> List[List[str]]:
    queue = []
    queue.append([current.name])
    results = []

    while len(queue) > 0:
        path = queue.pop(0)
        name = path[-1]
        if name == "end":
            results.append(path)
        else:
            for n in map[name].edges:
                if n != "start" and (n.isupper() or (n.islower() and n not in path)):
                    p = path.copy()
                    p.append(n)
                    queue.append(p)
    return results


def count_paths(lines: List[str]) -> int:
    map = _parse_input(lines)
    return len(_bfs(map, map["start"]))


def _not_in_path_twice(path: List[str]) -> bool:
    result = {}
    for node in path:
        if node.islower() and node not in ["start", "end"]:
            if node in result:
                result[node] += 1
            else:
                result[node] = 1

    count = 0
    bad = 0
    for k, v in result.items():
        if v == 2:
            count += 1
        elif v > 2:
            bad += 1
    return bad == 0 and (count == 1 or count == 0)


def _bfs2(map: Dict[str, Node], current: Node) -> List[List[str]]:
    queue = deque()
    queue.append([current.name])
    results = []

    while queue:
        path = queue.popleft()
        name = path[-1]
        if name == "end":
            results.append(path)
        else:
            for n in map[name].edges:
                if n != "start" and (n.isupper() or (n.islower() and _not_in_path_twice(path))):
                    p = path.copy()
                    p.append(n)
                    queue.append(p)
    return results


def count_paths2(lines: List[str]) -> int:
    map = _parse_input(lines)
    return len(_bfs2(map, map["start"]))