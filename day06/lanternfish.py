from collections import defaultdict
from typing import List, Dict


def _step_one_day(fish_groups: Dict[int, int]) -> Dict[int, int]:
    next_group: Dict[int, int] = defaultdict(int)
    for fish, count in fish_groups.items():
        if fish == 0:
            next_group[6] += count
            next_group[8] = count
        else:
            next_group[fish - 1] += count
    return next_group


def count_fish_after_days(days: int, initial_state: List[int]) -> int:
    fish_groups: Dict[int, int] = defaultdict(int)
    for fish in initial_state:
        fish_groups[fish] += 1

    for _ in range(0, days):
        fish_groups = _step_one_day(fish_groups)
    return sum(v for v in fish_groups.values())
