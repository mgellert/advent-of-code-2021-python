from typing import List


def read_file() -> str:
    with open("../inputs/day11", "r") as file:
        return file.read()


def _parse_input(input: str) -> List[List[int]]:
    return [[int(char) for char in line] for line in input.split("\n")]


def _will_flash(octopi: List[List[int]]) -> (int, int):
    for i in range(0, len(octopi)):
        for j in range(0, len(octopi[i])):
            if octopi[i][j] > 9:
                return i, j
    return -1, -1


deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def _step(octopi: List[List[int]]) -> (List[List[int]], int):
    next_step: List[List[int]] = []
    for i in range(0, len(octopi)):
        next_step.append([])
        for j in range(0, len(octopi[i])):
            next_step[i].append(0)

    flashes = 0
    for i in range(0, len(octopi)):
        for j in range(0, len(octopi[i])):
            next_step[i][j] = octopi[i][j] + 1

    x, y = _will_flash(next_step)
    while x > -1:
        next_step[x][y] = 0
        flashes += 1
        for delta in deltas:
            i = x + delta[0]
            j = y + delta[1]
            if 0 <= i < len(octopi) and 0 <= j < len(octopi[i]) and next_step[i][j] != 0:
                next_step[i][j] += 1
        x, y = _will_flash(next_step)

    return next_step, flashes


def count_flashes(input: str, steps: int = 100) -> int:
    octopi = _parse_input(input)
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


def count_sync(input: str) -> int:
    octopi = _parse_input(input)
    steps = 0
    while True:
        octopi, _ = _step(octopi)
        steps += 1
        if _is_all_zero(octopi):
            break
    return steps
