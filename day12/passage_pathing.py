from collections import deque, defaultdict, Counter
from typing import List, Dict, Set, Callable

SearchFn = Callable[[str, List[str]], bool]


def parse_input(lines: List[str]) -> Dict[str, Set[str]]:
    cave_system = defaultdict(set)
    for line in lines:
        node1, node2 = line.split("-")
        cave_system[node1].add(node2)
        cave_system[node2].add(node1)
    return cave_system


def _bfs(cave_system: Dict[str, Set[str]], path_search: SearchFn, current: str = "start") -> List[List[str]]:
    queue = deque()
    queue.append([current])
    results = []

    while queue:
        path = queue.popleft()
        name = path[-1]
        if name == "end":
            results.append(path)
        else:
            for n in cave_system[name]:
                is_not_in_path = path_search(n, path)
                if n != "start" and (n.isupper() or (n.islower() and is_not_in_path)):
                    queue.append(path + [n])
    return results


def _simple_path_search(n: str, path: List[str]):
    return n not in path


def _path_search_more_allowed(n: str, path: List[str]) -> bool:
    full_path = [*path, n]
    result = defaultdict(int)
    more_than_twice = 0

    for node in full_path:
        if node.islower() and node not in ["start", "end"]:
            result[node] += 1
            count = result[node]
            if count >= 2:
                more_than_twice += 1
                if count > 2 or more_than_twice > 1:
                    return False
    return True


def count_paths(cave_system: Dict[str, Set[str]]) -> int:
    return len(_bfs(cave_system, _simple_path_search))


def count_paths2(cave_system: Dict[str, Set[str]]) -> int:
    return len(_bfs(cave_system, _path_search_more_allowed))
