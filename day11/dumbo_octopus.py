from typing import List


def parse_input(raw: str) -> List[List[int]]:
    return [[int(char) for char in line] for line in raw.split("\n")]


def _will_flash(octopi: List[List[int]]) -> (int, int):
    for i in range(0, len(octopi)):
        for j in range(0, len(octopi[i])):
            if octopi[i][j] > 9:
                return i, j
    return None, None


deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def _step(octopi: List[List[int]]) -> (List[List[int]], int):
    next_step: List[List[int]] = [[0] * len(octopi[i]) for i in range(len(octopi))]

    # increase energy level
    for i in range(0, len(octopi)):
        for j in range(0, len(octopi[i])):
            next_step[i][j] = octopi[i][j] + 1

    flashes = 0
    x, y = _will_flash(next_step)
    while x is not None:
        next_step[x][y] = 0
        flashes += 1
        for delta in deltas:
            i = x + delta[0]
            j = y + delta[1]
            if 0 <= i < len(octopi) and 0 <= j < len(octopi[i]) and next_step[i][j] != 0:
                next_step[i][j] += 1
        x, y = _will_flash(next_step)

    return next_step, flashes


def count_flashes(octopi: List[List[int]], steps: int = 100) -> int:
    total = 0
    for _ in range(0, steps):
        octopi, flashes = _step(octopi)
        total += flashes
    return total


def _is_all_zero(octopi: List[List[int]]) -> bool:
    for i in range(0, len(octopi)):
        for j in range(0, len(octopi[i])):
            if octopi[i][j] != 0:
                return False
    return True


def count_sync(octopi: List[List[int]]) -> int:
    steps = 0
    while True:
        octopi, _ = _step(octopi)
        steps += 1
        if _is_all_zero(octopi):
            return steps
