import re
from typing import List, Tuple

Command = Tuple[str, int]

command_re = re.compile("(forward|down|up) (\\d+)")

UP = "up"
DOWN = "down"
FORWARD = "forward"


def parse_commands(lines: List[str]) -> List[Command]:
    commands = []
    for line in lines:
        m = command_re.match(line)
        commands.append((m.group(1), int(m.group(2))))
    return commands


def calculate_position(commands: List[Command]) -> int:
    horizontal = 0
    depth = 0
    for command, amount in commands:
        if command == FORWARD:
            horizontal += amount
        elif command == DOWN:
            depth += amount
        elif command == UP:
            depth -= amount
    return horizontal * depth


def calculate_aim(commands: List[Command]) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for command, amount in commands:
        if command == FORWARD:
            horizontal += amount
            depth += aim * amount
        elif command == DOWN:
            aim += amount
        elif command == UP:
            aim -= amount
    return horizontal * depth
