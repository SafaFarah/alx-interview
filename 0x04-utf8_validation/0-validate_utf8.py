#!/usr/bin/python3
""" Check if the given list of integers represents valid UTF-8 encoding."""


def validUTF8(data):
    """
    Check if the given list of integers represents valid UTF-8 encoding.

    data: List of integers where each integer represents a byte
    return: True if valid UTF-8 encoding, otherwise False
    """
    try:
        bytes(data).decode('utf-8')
    except (ValueError, UnicodeDecodeError):
        return False
    return True
