import unittest
from dataclasses import dataclass

from day16.packet_decoder import convert_to_bin, read_input, sum_packet_versions, calculate_packet_value


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
            TestCase(input=read_input(), expected=1002)
        ]

        for case in testcases:
            actual = sum_packet_versions(case.input)
            self.assertEqual(case.expected, actual)

    def test_calculate_packet_value(self):
        testcases = [
            TestCase(input="D2FE28", expected=2021),
            TestCase(input="C200B40A82", expected=3),
            TestCase(input="04005AC33890", expected=54),
            TestCase(input="880086C3E88112", expected=7),
            TestCase(input="CE00C43D881120", expected=9),
            TestCase(input="D8005AC2A8F0", expected=1),
            TestCase(input="F600BC2D8F", expected=0),
            TestCase(input="9C005AC2F8F0", expected=0),
            TestCase(input="9C0141080250320F1802104A08", expected=1),
            TestCase(input=read_input(), expected=1673210814091)
        ]

        for case in testcases:
            actual = calculate_packet_value(case.input)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
