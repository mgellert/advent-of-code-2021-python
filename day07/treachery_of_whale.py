from typing import List, Callable


def find_optimal_pos(crab_positions: List[int], fuel_burn: Callable[[int, int], int]) -> int:
    return min(
        # fuel cost for all crabs for specific alignment position
        sum(fuel_burn(crab_pos, aligned_pos) for crab_pos in crab_positions)
        # iterate through all possible alignment positions
        for aligned_pos in range(min(crab_positions), max(crab_positions) + 1)
    )


def constant(a: int, b: int) -> int:
    return abs(a - b)


def increasing(a: int, b: int) -> int:
    n = abs(a - b)
    return int(n * (1 + n) / 2)
