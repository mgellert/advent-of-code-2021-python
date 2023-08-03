from _decimal import Decimal, ROUND_HALF_UP
from statistics import mean
from typing import List


def _find_most_common_bit(diagnostics: List[str], col: int) -> str:
    column = [int(line[col]) for line in diagnostics]
    # cannot use round() because round(0.5) = 0
    rounded = Decimal(mean(column)).to_integral_value(rounding=ROUND_HALF_UP)
    return str(int(rounded))


def _invert_bit(bit: str) -> str:
    return "0" if bit == "1" else "1"


def part_1(diagnostics: List[str]) -> int:
    row_len = len(diagnostics[0])
    gamma = ""
    epsilon = ""
    for i in range(0, row_len):
        most_common_bit = _find_most_common_bit(diagnostics, i)
        gamma += most_common_bit
        epsilon += _invert_bit(most_common_bit)
    return int(gamma, 2) * int(epsilon, 2)


def _filter_diagnostics(diagnostics: List[str], row_len: int, invert: bool = False) -> str:
    for i in range(0, row_len):
        most_common_bit = _find_most_common_bit(diagnostics, i)
        if invert:
            most_common_bit = _invert_bit(most_common_bit)
        diagnostics = [bit for bit in diagnostics if bit[i] == most_common_bit]
        if len(diagnostics) == 1:
            return diagnostics[0]
    raise Exception("Could not reduce diagnostics to one number")


def part_2(diagnostics: List[str]) -> int:
    row_len = len(diagnostics[0])
    oxygen = _filter_diagnostics(diagnostics, row_len)
    co2_scrubber = _filter_diagnostics(diagnostics, row_len, invert=True)

    return int(oxygen, 2) * int(co2_scrubber, 2)
