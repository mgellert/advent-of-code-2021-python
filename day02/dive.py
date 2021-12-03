import re
from typing import List, Tuple

command_re = re.compile("(forward|down|up) (\\d+)")


def read_file(name: str) -> List[str]:
    with open(f"../inputs/{name}", "r") as file:
        return [line for line in file]


def _parse_commands(lines: List[str]) -> List[Tuple[str, int]]:
    commands = []
    for line in lines:
        m = command_re.match(line)
        commands.append((m.group(1), int(m.group(2))))
    return commands


def calculate_position(lines: List[str]) -> int:
    horizontal = 0
    depth = 0
    for command, amount in _parse_commands(lines):
        if command == "forward":
            horizontal += amount
        elif command == "down":
            depth += amount
        elif command == "up":
            depth -= amount
    return horizontal * depth


def calculate_aim(lines: List[str]) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for command, amount in _parse_commands(lines):
        if command == "forward":
            horizontal += amount
            depth += aim * amount
        elif command == "down":
            aim += amount
        elif command == "up":
            aim -= amount
    return horizontal * depth
