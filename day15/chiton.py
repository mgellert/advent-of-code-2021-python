from collections import defaultdict
from queue import PriorityQueue
from typing import List, Tuple, Dict

Cavern = List[List[int]]


def _parse_area(lines: List[str]) -> Cavern:
    return [[int(j) for j in i.strip()] for i in lines]


def _get_vertex_with_risk(cavern: Cavern, x: int, y: int) -> Tuple[int, int, int]:
    return cavern[x][y], x, y


def _get_neighbours(cavern: Cavern, x: int, y: int) -> List[Tuple[int, int, int]]:
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if x < len(cavern) - 1:
        neighbours.append((x + 1, y))
    if y < len(cavern[x]) - 1:
        neighbours.append((x, y + 1))
    return [_get_vertex_with_risk(cavern, *v) for v in neighbours]


# Dijkstra's algorithm
def _find_path(area: Cavern) -> int:
    queue = PriorityQueue()
    queue.put(_get_vertex_with_risk(area, 0, 0))

    visited = set()

    weights: Dict[Tuple[int, int], int] = defaultdict(lambda: 9999)
    weights[(0, 0)] = 0

    while not queue.empty():
        weight, x, y = queue.get()
        visited.add((x, y))

        for neighbor in _get_neighbours(area, x, y):
            weight, nx, ny = neighbor
            if (nx, ny) not in visited:
                old_cost = weights[(nx, ny)]
                new_cost = weights[(x, y)] + weight
                if new_cost < old_cost:
                    queue.put((new_cost, nx, ny))
                    weights[(nx, ny)] = new_cost

    return weights[len(area) - 1, len(area[0]) - 1]


def find_lowest_total_risk_path(lines: List[str]):
    return _find_path(_parse_area(lines))


def _full_cavern(cavern: Cavern) -> Cavern:
    height = len(cavern)
    width = len(cavern[0])

    full_cavern = [[0 for _ in range(width * 5)] for _ in range(height * 5)]

    for k in range(0, 5):
        for l in range(0, 5):
            for i in range(height):
                for j in range(width):
                    weight = cavern[i][j] + k + l
                    if weight > 9:
                        weight -= 9
                    full_cavern[k * height + i][l * width + j] = weight

    return full_cavern


def find_lowest_total_risk_path_in_large_cavern(lines: List[str]):
    return _find_path(_full_cavern(_parse_area(lines)))
