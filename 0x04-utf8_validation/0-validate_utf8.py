#!/usr/bin/python3
"""This is a module for the UTF-8 Validation interview question"""


def validUTF8(data):
    """a method to implement UTF-8 validation for a given data"""
    length = len(data)

    size = 0
    while size < length:
        if (data[size] & (1 << 7)) == 0:
            size += 1
            continue

        a = 0
        while (data[size] & (1 << (7 - a))) > 0 and a <= 5:
            a += 1

        if a == 1 or a > 4:
            return False

        for i in range(1, a):
            if size + i >= length:
                return False
            if (data[size + 1] & ((1 << 7) | (1 << 6))) != (1 << 7):
                return False
        size += a
    return True
