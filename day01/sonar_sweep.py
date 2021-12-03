from typing import List


def read_file_to_int(name: str) -> List[int]:
    with open(f"../inputs/{name}", "r") as file:
        return [int(line) for line in file]


def count_larger_measurements(measurements: List[int]) -> int:
    return sum([1 for a, b in list(zip(measurements[:-1], measurements[1:])) if b > a])
