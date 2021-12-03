from typing import List


def read_file_to_int(name: str) -> List[int]:
    with open(f"../inputs/{name}", "r") as file:
        return [int(line) for line in file]


def count_larger_measurements(measurements: List[int]) -> int:
    larger_count = 0
    prev = None
    for m in measurements:
        if prev and m > prev:
            larger_count += 1
        prev = m
    return larger_count
