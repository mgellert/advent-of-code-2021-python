from collections import deque
from functools import reduce

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def read_input() -> str:
    with open("../inputs/day16", "r") as file:
        return file.read()


def convert_to_bin(transmission: str) -> str:
    return "".join([hex_to_bin[c] for c in transmission])


def _slice_packet(binary: str) -> (int, str):
    version = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)
    if type_id == 4:
        # print(f"literal packet, version {version}")
        i = 3 + 3  # version: 3 bits + type id: 3 bits
        while binary[i] == "1":
            i += 5
        i += 5  # last packet
        return version, binary[i:]
    else:
        length_type_id = int(binary[6], 2)
        # print(f"operator packet, version {version}")
        if length_type_id == 0:
            packet_length = int(binary[7: 7 + 15], 2)
            binary = binary[7 + 15:]
            sum = version
            desired_len = len(binary) - packet_length
            while len(binary) != desired_len:
                version, binary = _slice_packet(binary)
                sum += version
            return sum, binary
        elif length_type_id == 1:
            packet_count = int(binary[7: 7 + 11], 2)
            binary = binary[7 + 11:]
            sum = version
            for _ in range(packet_count):
                version, binary = _slice_packet(binary)
                sum += version
            return sum, binary


def sum_packet_versions(transmission: str) -> int:
    binary = convert_to_bin(transmission)
    sum, _ = _slice_packet(binary)
    return sum


def _slice_packet_2(binary: str) -> (int, str):
    version = int(binary[:3], 2)
    type_id = int(binary[3:6], 2)

    if type_id == 4:
        # print(f"literal packet, version {version}")
        i = 3 + 3  # version: 3 bits + type id: 3 bits
        number = ""
        while binary[i] == "1":
            number += binary[i + 1: i + 5]
            i += 5
        number += binary[i + 1: i + 5]
        i += 5  # last packet
        return int(number, 2), binary[i:]
    else:
        length_type_id = int(binary[6], 2)
        # print(f"operator packet, version {version}")
        numbers = []

        if length_type_id == 0:
            packet_length = int(binary[7: 7 + 15], 2)
            binary = binary[7 + 15:]
            desired_len = len(binary) - packet_length
            while len(binary) != desired_len:
                number, binary = _slice_packet_2(binary)
                numbers.append(number)

        elif length_type_id == 1:
            packet_count = int(binary[7: 7 + 11], 2)
            binary = binary[7 + 11:]
            for _ in range(packet_count):
                number, binary = _slice_packet_2(binary)
                numbers.append(number)

        if type_id == 0:
            return sum(numbers), binary
        elif type_id == 1:
            return reduce(lambda x, y: x * y, numbers, 1), binary
        elif type_id == 2:
            return min(numbers), binary
        elif type_id == 3:
            return max(numbers), binary
        elif type_id == 5:
            return 1 if numbers[0] > numbers[1] else 0, binary
        elif type_id == 6:
            return 1 if numbers[0] < numbers[1] else 0, binary
        elif type_id == 7:
            return 1 if numbers[0] == numbers[1] else 0, binary


def calculate_packet_value(transmission: str) -> int:
    binary = convert_to_bin(transmission)
    value, _ = _slice_packet_2(binary)
    return value
