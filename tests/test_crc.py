import unittest

from crc import append_crc, calcrc, verify_packet


class CrcTests(unittest.TestCase):
    DATA = [0xA1, 0x03, 0x00, 0x00, 0x00, 0x0F]

    def test_known_crc_vector(self):
        self.assertEqual(calcrc(self.DATA), (0x6E, 0x1D))

    def test_append_uses_modbus_low_byte_first_order(self):
        self.assertEqual(append_crc(self.DATA), self.DATA + [0x1D, 0x6E])

    def test_appended_packet_verifies(self):
        self.assertEqual(verify_packet(append_crc(self.DATA)), (0x6E, 0x1D, True))

    def test_corrupted_packet_fails_verification(self):
        packet = append_crc(self.DATA)
        packet[-1] ^= 0x01
        self.assertEqual(verify_packet(packet), (0x6E, 0x1D, False))

    def test_bytes_input_returns_bytes(self):
        packet = append_crc(bytes(self.DATA))
        self.assertIsInstance(packet, bytes)
        self.assertTrue(verify_packet(packet)[2])

    def test_rejects_empty_data(self):
        with self.assertRaises(ValueError):
            append_crc([])

    def test_rejects_short_packet(self):
        with self.assertRaises(ValueError):
            verify_packet([0x01, 0x02])

    def test_rejects_invalid_byte(self):
        with self.assertRaises(ValueError):
            append_crc([0x100])


if __name__ == "__main__":
    unittest.main()
