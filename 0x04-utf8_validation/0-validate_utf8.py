#!/usr/bin/python3
""" UTF-8 Validation """

def validUTF8(data):

    number_bytes = 0

    ms1 = 1 << 7
    ms2 = 1 << 6

    for i in data:

        buffer = 1 << 7

        if number_bytes == 0:

            while buffer & i:
                number_bytes += 1
                buffer = buffer >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & ms1 and not (i & ms2)):
                    return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
