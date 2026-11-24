"""CRC-16 helpers for the serial communication experiments.

The implementation uses polynomial 0xA001 with an initial value of 0xFFFF.
Packets append the CRC low byte first (Modbus wire order).
"""


def calcrc(data, ldata=None):
    """Return (crc_high, crc_low) for the first ldata + 1 bytes.

    ldata is retained for compatibility with the original project API.
    When omitted, all bytes in data are processed.
    """
    values = list(data)
    if ldata is None:
        ldata = len(values) - 1
    if not values or not isinstance(ldata, int) or ldata < 0 or ldata >= len(values):
        raise ValueError("CRC input must contain at least one byte and ldata must be a valid index.")

    selected = values[: ldata + 1]
    if any(not isinstance(value, int) or not 0 <= value <= 0xFF for value in selected):
        raise ValueError("CRC input values must be integers between 0 and 255.")

    crc = 0xFFFF
    for value in selected:
        crc ^= value
        for _ in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1

    return (crc >> 8) & 0xFF, crc & 0xFF


def append_crc(data_bytes):
    """Append a Modbus-order CRC to bytes-like input or an iterable of bytes.

    Returns bytes when the input is bytes-like, otherwise a list.
    """
    values = list(data_bytes)
    if not values:
        raise ValueError("Cannot append a CRC to an empty packet.")
    if any(not isinstance(value, int) or not 0 <= value <= 0xFF for value in values):
        raise ValueError("Packet values must be integers between 0 and 255.")

    crc_high, crc_low = calcrc(values)
    packet = values + [crc_low, crc_high]
    return bytes(packet) if isinstance(data_bytes, (bytes, bytearray, memoryview)) else packet


def verify_packet(packet_bytes):
    """Return (crc_high, crc_low, is_valid) for a packet with trailing CRC."""
    packet = list(packet_bytes)
    if len(packet) < 3:
        raise ValueError("A packet must contain at least one data byte and two CRC bytes.")
    if any(not isinstance(value, int) or not 0 <= value <= 0xFF for value in packet):
        raise ValueError("Packet values must be integers between 0 and 255.")

    crc_high, crc_low = calcrc(packet[:-2])
    is_valid = packet[-2:] == [crc_low, crc_high]
    return crc_high, crc_low, is_valid


if __name__ == "__main__":
    raw = input("Enter hex values (space separated): ").split()
    try:
        values = [int(value, 16) for value in raw]
        if len(values) >= 3:
            crc_high, crc_low, valid = verify_packet(values)
            print(f"Calculated CRC (low byte first): {crc_low:02X} {crc_high:02X}")
            print("Data is Intact" if valid else "Data is varied!")
        else:
            crc_high, crc_low = calcrc(values)
            print(f"Calculated CRC: high={crc_high:02X}, low={crc_low:02X}")
    except ValueError as error:
        print(f"Invalid input: {error}")
