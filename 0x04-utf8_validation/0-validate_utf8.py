#!/usr/bin/python3
""" Check if the given list of integers represents valid UTF-8 encoding."""


def validUTF8(data):
    """
    Check if the given list of integers represents valid UTF-8 encoding.

    data: List of integers where each integer represents a byte
    return: True if valid UTF-8 encoding, otherwise False
    """
    n_bytes = 0
    for byte in data:
        if n_bytes == 0:
            if (byte & 0b10000000) == 0b00000000:
                n_bytes = 0  # 1-byte character
            elif (byte & 0b11100000) == 0b11000000:
                n_bytes = 1  # 2-byte character
            elif (byte & 0b11110000) == 0b11100000:
                n_bytes = 2  # 3-byte character
            elif (byte & 0b11111000) == 0b11110000:
                n_bytes = 3  # 4-byte character
            else:
                return False  # Invalid start byte
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False  # Invalid continuation byte
            n_bytes -= 1

    return n_bytes == 0
