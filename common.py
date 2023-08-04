from typing import List


def read_file_to_ints(name: str) -> List[int]:
    with open(f"../inputs/{name}", "r") as file:
        return [int(line) for line in file]


def read_lines(name: str) -> List[str]:
    with open(f"../inputs/{name}", "r") as file:
        return [line.strip() for line in file.readlines()]


def read_file(name: str) -> str:
    with open(f"../inputs/{name}", "r") as file:
        return file.read()
