import re
from typing import List, Tuple, Dict, Set

line_re = re.compile("([\\w ]+) \\| ([\\w ]+)")
wanted_lengths = (2, 3, 4, 7)


def parse_line(line: str) -> Tuple[List[str], List[str]]:
    readings, outputs = line_re.match(line).groups()
    return readings.split(), outputs.split()


def part_1(entries: List[Tuple[List[str], List[str]]]) -> int:
    return sum(sum(1 for output in outputs if len(output) in wanted_lengths) for _, outputs in entries)


def _find_key(entry: List[str]) -> Dict[int, Set[str]]:
    keys: Dict[int, Set[str]] = {}
    while len(keys) < 10:
        for digit in entry:
            chars = set(digit)
            if len(digit) == 2:
                keys[1] = chars
            elif len(chars) == 5 and keys.get(5) and len(keys[5].difference(chars)) == 2:
                keys[2] = chars
            elif len(chars) == 5 and keys.get(1) and keys[1].issubset(chars):
                keys[3] = chars
            elif len(digit) == 4:
                keys[4] = chars
            elif len(chars) == 5 and keys.get(6) and len(keys[6].difference(chars)) == 1:
                keys[5] = chars
            elif len(chars) == 6 and keys.get(1) and not keys[1].issubset(chars):
                keys[6] = chars
            elif len(digit) == 3:
                keys[7] = chars
            elif len(digit) == 7:
                keys[8] = chars
            elif len(chars) == 6 and keys.get(4) and keys[4].issubset(chars):
                keys[9] = chars
            elif len(chars) == 6 and keys.get(8) and chars.issubset(keys[8]):
                keys[0] = chars
    return keys


def _decipher(readings: List[str], outputs: List[str]) -> int:
    deciphered = {frozenset(chars): str(digit) for digit, chars in _find_key(readings + outputs).items()}
    return int("".join(deciphered[frozenset(set(i))] for i in outputs))


def part_2(entries: List[Tuple[List[str], List[str]]]) -> int:
    return sum(_decipher(readings, output) for readings, output in entries)
