from collections import defaultdict
from queue import PriorityQueue
from typing import List, Tuple, Dict


def read_input() -> List[str]:
    with open("../inputs/day15", "r") as file:
        return file.readlines()


def _parse_area(input: List[str]) -> List[List[int]]:
    return [[int(j) for j in i.strip()] for i in input]


def _get_vertex_with_risk(area: List[List[int]], y: int, x: int) -> Tuple[int, int, int]:
    return area[y][x], y, x


def _get_neighbours(area: List[List[int]], y: int, x: int) -> List[Tuple[int, int, int]]:
    neighbours = []
    if y > 0:
        neighbours.append((y - 1, x))
    if x > 0:
        neighbours.append((y, x - 1))
    if y < len(area) - 1:
        neighbours.append((y + 1, x))
    if x < len(area[y]) - 1:
        neighbours.append((y, x + 1))
    return [_get_vertex_with_risk(area, *v) for v in neighbours]


def find_lowest_total_risk_path(input: List[str]):
    area = _parse_area(input)

    pq = PriorityQueue()
    pq.put(_get_vertex_with_risk(area, 0, 0))

    visited = set()

    weights: Dict[Tuple[int, int], int] = defaultdict(lambda: 999999999999999999)
    weights[(0, 0)] = 0

    while not pq.empty():
        weight, y, x = pq.get()
        visited.add((y, x))

        for neighbor in _get_neighbours(area, y, x):
            weight, ny, nx = neighbor
            if (ny, nx) not in visited:
                old_cost = weights[(ny, nx)]
                new_cost = weights[(y, x)] + weight
                if new_cost < old_cost:
                    pq.put((new_cost, ny, nx))
                    weights[(ny, nx)] = new_cost

    return weights[len(area) - 1, len(area[0]) - 1]


def _enlarge_area(area: List[List[int]]) -> List[List[int]]:
    enlarged = [[0 for _ in range(len(area[0]) * 5)] for _ in range(len(area) * 5)]

    height = len(area)
    width = len(area[0])

    for k in range(0, 5):
        for l in range(0, 5):
            for i in range(height):
                for j in range(width):
                    weight = area[i][j] + k + l
                    if weight > 9:
                        weight -= 9
                    enlarged[k * height + i][l * width + j] = weight
    return enlarged


def find_lowest_total_risk_path_in_large_area(input: List[str]):
    area = _enlarge_area(_parse_area(input))

    pq = PriorityQueue()
    pq.put(_get_vertex_with_risk(area, 0, 0))

    visited = set()

    weights: Dict[Tuple[int, int], int] = defaultdict(lambda: 999999999999999999)
    weights[(0, 0)] = 0

    while not pq.empty():
        weight, y, x = pq.get()
        visited.add((y, x))

        for neighbor in _get_neighbours(area, y, x):
            weight, ny, nx = neighbor
            if (ny, nx) not in visited:
                old_cost = weights[(ny, nx)]
                new_cost = weights[(y, x)] + weight
                if new_cost < old_cost:
                    pq.put((new_cost, ny, nx))
                    weights[(ny, nx)] = new_cost

    return weights[len(area) - 1, len(area[0]) - 1]
