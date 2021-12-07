from typing import List, Callable


def read_file() -> List[int]:
    with open("../inputs/day07", "r") as file:
        return [int(x) for x in file.read().strip().split(",")]


def find_optimal_pos(positions: List[int], fuel_consumption: Callable[[int, int], int]) -> int:
    fuel_consumptions = []
    for p in range(min(positions), max(positions) + 1):
        fuel = [fuel_consumption(p, i) for i in positions]
        fuel_consumptions.append(sum(fuel))
    return min(fuel_consumptions)


def constant(a: int, b: int) -> int:
    return abs(a - b)


def increasing(a: int, b: int) -> int:
    n = abs(a - b)
    return int(n * (1 + n) / 2)
