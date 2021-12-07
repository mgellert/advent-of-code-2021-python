from typing import List, Dict


def read_file() -> List[int]:
    with open("../inputs/day06", "r") as file:
        return [int(x) for x in file.read().strip().split(",")]


def _aggregate_initial(initial: List[int]) -> Dict[int, int]:
    groups = {}
    for fish in initial:
        if fish in groups:
            groups[fish] += 1
        else:
            groups[fish] = 1
    return groups


def _step_forward(groups: Dict[int, int]) -> Dict[int, int]:
    next_group = {}
    for fish, count in groups.items():
        if fish == 0:
            x = next_group.get(6) or 0
            next_group[6] = x + count
            next_group[8] = count
        else:
            x = next_group.get(fish - 1) or 0
            next_group[fish - 1] = x + count
    s1 = sum([v for v in groups.values()])
    s2 = sum([v for v in next_group.values()])
    return next_group


def count_fish_after_days(days: int, initial: List[int]) -> int:
    groups = _aggregate_initial(initial)
    for _ in range(0, days):
        groups = _step_forward(groups)
    return sum([v for v in groups.values()])
