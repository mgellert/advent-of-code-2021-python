import unittest
from dataclasses import dataclass

from day16.packet_decoder import convert_to_bin, read_input, sum_packet_versions


@dataclass
class TestCase:
    input: str
    expected: int


class PacketDecoderTest(unittest.TestCase):
    def test_sum_packet_versions(self):
        testcases = [
            TestCase(input="D2FE28", expected=6),
            TestCase(input="38006F45291200", expected=9),
            TestCase(input="EE00D40C823060", expected=14),
            TestCase(input="8A004A801A8002F478", expected=16),
            TestCase(input="620080001611562C8802118E34", expected=12),
            TestCase(input="C0015000016115A2E0802F182340", expected=23),
            TestCase(input="A0016C880162017C3686B18A3D4780", expected=31),
            TestCase(input=read_input(), expected=1002),
        ]

        for case in testcases:
            actual = sum_packet_versions(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
