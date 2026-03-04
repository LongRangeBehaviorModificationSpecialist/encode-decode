# !/usr/bin/env python3

import string

from results import Results


class RotateString:

    def rotate_string(self, input_string: str, n: int) -> str:
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        n = int(n)
        trans = str.maketrans(
            lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
        rotated_string = str.translate(input_string, trans)
        Results.print_results(self, results=rotated_string)


"""

VGhpcyBpcyBhIHRlc3Qgc3RyaW5nIHRoYXQgd2FzIGVuY29kZWQgaW4gQmFzZTY0Lg==

ASCII : mikespon

Rot13 :  zvxr fcba

Base64 : bWlrZSBzcG9u

Binary : 01101101 01101001 01101011 01100101 00100000 01110011 01110000 01101111 01101110

Hex : 6D 69 6B 65 20 73 70 6F 6E

Dec : 109 105 107 101 32 115 112 111 110

Oct : 155 151 153 145 40 163 160 157 156

Morse Code : -- .. -.- .  ... .--. --- -.

"""