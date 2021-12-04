from typing import List, Dict


def read_file(name: str) -> List[str]:
    with open(f"../inputs/{name}", "r") as file:
        return [line for line in file]


def _calculate_stats(lines: List[str]) -> Dict[int, Dict[str, int]]:
    stats = {}
    for line in lines:
        for i, c in enumerate(line.strip()):
            if i not in stats:
                stats[i] = {}
            if c not in stats[i]:
                stats[i][c] = 0
            stats[i][c] += 1
    return stats


def _calculate_bit_occurrence(stats: Dict[int, Dict[str, int]]) -> (str, str):
    gamma = ""
    epsilon = ""
    for i, occurrence in stats.items():
        if occurrence["1"] > occurrence["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            epsilon += "1"
            gamma += "0"
    return gamma, epsilon


def calculate_power_consumption(lines: List[str]) -> int:
    stats = _calculate_stats(lines)
    gamma, epsilon = _calculate_bit_occurrence(stats)
    return int(gamma, 2) * int(epsilon, 2)


def _calculate_oxygen_rating(lines: List[str], pos: int = 0) -> int:
    if len(lines) == 1:
        return int(lines[0], 2)

    stats = _calculate_stats(lines)

    keep = "1"
    if stats[pos]["0"] > stats[pos]["1"]:
        keep = "0"
    lines = [line for line in lines if line[pos] == keep]
    return _calculate_oxygen_rating(lines, pos + 1)


def _calculate_co2_scrubber_rating(lines: List[str], pos: int = 0) -> int:
    if len(lines) == 1:
        return int(lines[0], 2)

    stats = _calculate_stats(lines)

    keep = "1"
    if stats[pos]["0"] <= stats[pos]["1"]:
        keep = "0"
    lines = [line for line in lines if line[pos] == keep]
    return _calculate_co2_scrubber_rating(lines, pos + 1)


def find_life_support_rating(lines: List[str]) -> int:
    oxygen_rating = _calculate_oxygen_rating(lines)
    co2_scrubber_rating = _calculate_co2_scrubber_rating(lines)
    return oxygen_rating * co2_scrubber_rating
