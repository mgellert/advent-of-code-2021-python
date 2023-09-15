import re
from collections import defaultdict
from typing import List, Dict, Tuple

rule_re = re.compile("^([A-Z]{2}) -> ([A-Z])$")

Rules = Dict[str, Tuple[str, str]]


def _parse_polymer_template(line: str) -> Dict[str, int]:
    return {line[i:i + 2]: 1 for i in range(len(line) - 1)}


def _parse_rules(lines: List[str]) -> Rules:
    rules = {}
    for line in lines:
        match = rule_re.match(line)
        if match:
            key = match[1]
            value = match[2]
            rules[key] = (key[0] + value, value + key[1])
    return rules


def _apply_rules(polymer: Dict[str, int], rules: Rules) -> Dict[str, int]:
    next_polymer = defaultdict(int)
    for pair, count in polymer.items():
        left, right = rules[pair]
        next_polymer[left] += count
        next_polymer[right] += count
    return next_polymer


def _most_and_least_common_count(polymer: Dict[str, int], original_polymer: str) -> (int, int):
    counts = defaultdict(int)

    # first and last characters are only counted once
    # example:             ABA -> AB, BA -> A: 2, B: 2         -> divide by 2 -> A: 1, B: 1
    # correct calculation: ABA -> AB, BA -> A: 2 + 1 + 1, B: 2 -> divide by 2 -> A: 2, B: 1
    counts[original_polymer[0]] += 1
    counts[original_polymer[-1]] += 1

    for pair, count in polymer.items():
        first, second = pair
        counts[first] += count
        counts[second] += count
    return max(counts.values()) // 2, min(counts.values()) // 2


def most_and_least_common(lines: List[str], steps: int) -> int:
    polymer = _parse_polymer_template(lines[0])
    rules = _parse_rules(lines)
    for _ in range(0, steps):
        polymer = _apply_rules(polymer, rules)

    most_common, least_common = _most_and_least_common_count(polymer, original_polymer=lines[0])
    return most_common - least_common
