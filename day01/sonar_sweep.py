from typing import List


def read_file_to_int(name: str) -> List[int]:
    with open(f"../inputs/{name}", "r") as file:
        return [int(line) for line in file]


def count_larger_measurements(measurements: List[int]) -> int:
    return sum([1 for a, b in list(zip(measurements, measurements[1:])) if b > a])


def count_larger_sums(measurements: List[int]) -> int:
    triplets = list(zip(measurements, measurements[1:], measurements[2:]))
    return sum([1 for a, b in list(zip(triplets, triplets[1:])) if sum(b) > sum(a)])
