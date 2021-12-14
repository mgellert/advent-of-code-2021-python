import re
from collections import defaultdict
from typing import List, Dict, Tuple

rule_re = re.compile("^([A-Z]{2}) -> ([A-Z]{1})$")


def read_input() -> List[str]:
    with open("../inputs/day14", "r") as file:
        return file.readlines()


def _parse_polymer_template(lines: List[str]) -> Dict[str, int]:
    first_line = lines[0].strip()
    polymer = {}
    for i in range(0, len(first_line) - 1):
        polymer[first_line[i:i + 2]] = 1
    return polymer


def _parse_rules(lines: List[str]) -> Dict[str, Tuple[str, str]]:
    rules = {}
    for line in lines:
        match = rule_re.match(line)
        if match:
            key = match[1]
            value = match[2]
            rules[match[1]] = (key[0] + value, value + key[1])
    return rules


def _apply_rules(polymer: Dict[str, int], rules: Dict[str, Tuple[str, str]]) -> Dict[str, int]:
    next_polymer = defaultdict(int)
    for pair, count in polymer.items():
        left, right = rules[pair]
        next_polymer[left] += count
        next_polymer[right] += count
    return next_polymer


def _most_and_least_common_count(polymer: Dict[str, int], first: str, last: str) -> (int, int):
    counts = defaultdict(int)
    counts[first] += 1
    counts[last] += 1

    for pair, count in polymer.items():
        first, second = pair
        counts[first] += count
        counts[second] += count
    return max(counts.values()) // 2, min(counts.values()) // 2


def most_and_least_common(lines: List[str], steps: int = 10) -> int:
    first = lines[0].strip()[0]
    last = lines[0].strip()[-1]
    polymer = _parse_polymer_template(lines)
    rules = _parse_rules(lines)
    for _ in range(0, steps):
        polymer = _apply_rules(polymer, rules)
    most_common, least_common = _most_and_least_common_count(polymer, first, last)
    return most_common - least_common
