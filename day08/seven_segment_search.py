import re
from typing import List, Tuple, Dict, Set


def read_file() -> List[str]:
    with open("../inputs/day08", "r") as file:
        return file.readlines()


line_re = re.compile(
    "(\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) (\\w+) \\| (\\w+) (\\w+) (\\w+) (\\w+)")


def _parse_line(line: str) -> Tuple[List[str], List[str]]:
    m = line_re.match(line)
    readings = []
    outputs = []
    for i in range(1, 11):
        readings.append(m[i])
    for i in range(11, 15):
        outputs.append(m[i])
    return readings, outputs


def count_simple_digits(lines: List[str]) -> int:
    count = 0
    wanted_lens = [2, 3, 4, 7]
    for line in lines:
        _, outputs = _parse_line(line)
        for output in outputs:
            if len(output) in wanted_lens:
                count += 1
    return count


def _to_set(a: str) -> Set[str]:
    return {c for c in a}


def _decipher_digits(all_ciphers: List[str]) -> Dict[int, Set[str]]:
    deciphered: Dict[int, Set[str]] = {}
    while len(deciphered) < 10:
        for cipher in all_ciphers:
            cipher_chars: Set[str] = _to_set(cipher)
            if len(cipher) == 2:
                deciphered[1] = cipher_chars
            elif deciphered.get(5) and len(deciphered[5].difference(cipher_chars)) == 2 and len(cipher_chars) == 5:
                deciphered[2] = cipher_chars
            elif deciphered.get(5) and len(deciphered[5].difference(cipher_chars)) == 1 and len(cipher_chars) == 5:
                deciphered[3] = cipher_chars
            elif len(cipher) == 4:
                deciphered[4] = cipher_chars
            elif deciphered.get(6) and len(deciphered[6].difference(cipher_chars)) == 1 and len(cipher_chars) == 5:
                deciphered[5] = cipher_chars
            elif deciphered.get(1) and deciphered.get(4) and deciphered.get(7) and not \
                    deciphered[1].issubset(cipher_chars) and not deciphered[4].issubset(cipher_chars) and not \
                    deciphered[7].issubset(cipher_chars) and len(cipher_chars) == 6:
                deciphered[6] = cipher_chars
            elif len(cipher) == 3:
                deciphered[7] = cipher_chars
            elif len(cipher) == 7:
                deciphered[8] = cipher_chars
            elif deciphered.get(8) and deciphered.get(4) and cipher_chars.issubset(deciphered[8]) and \
                    deciphered[4].issubset(cipher_chars) and len(cipher_chars) == 6:
                deciphered[9] = cipher_chars
            elif deciphered.get(8) and deciphered.get(7) and cipher_chars.issubset(deciphered[8]) and \
                    deciphered[7].issubset(cipher_chars) and len(cipher_chars) == 6:
                deciphered[0] = cipher_chars
    return deciphered


def _decipher(readings: List[str], outputs: List[str]) -> int:
    all_ciphers = readings + outputs
    deciphered = {frozenset(v): k for k, v in _decipher_digits(all_ciphers).items()}
    result = 0
    m = 1000
    for i in outputs:
        result += m * deciphered[frozenset(_to_set(i))]
        m = int(m / 10)
    return result


def sum_output_values(lines: List[str]) -> int:
    sum = 0
    for line in lines:
        readings, outputs = _parse_line(line)
        sum += _decipher(readings, outputs)
    return sum
