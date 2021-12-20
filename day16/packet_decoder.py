from collections import deque

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
