#!/usr/bin/python3
"""UTF-8validation"""


def validUTF8(data):
    """determines if given data set represents valid UTF-8 encoding"""
    total_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6
    for byte in data:
        mask = 1 << 7
        if total_bytes == 0:
            while mask & byte:
                total_bytes += 1
                mask >>= 1

            if total_bytes == 0:
                continue
            if total_bytes == 1 or total_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False
        total_bytes -= 1
    return total_bytes == 0
