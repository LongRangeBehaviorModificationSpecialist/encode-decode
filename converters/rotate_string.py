# !/usr/bin/env python3
# DLU : 08-Aug-2026


import string
from rich.prompt import Prompt
from rich.traceback import install
from results import Results


install(show_locals=True)


class RotateString:


    def get_input_value(self) -> None:
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        return input


    def get_cipher_shift_value(self) -> int:
        n: int = Prompt.ask(
            "[white][-] Enter a numeric value for the shift you "
            "want to use"
        )
        return n


    def rotate_string(self) -> str:
        input = self.get_input_value()
        n = self.get_cipher_shift_value()
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        trans = str.maketrans(
            lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n]
        )
        rotated_string = str.translate(input, trans)
        Results.print_rotation_results(self, results=rotated_string)


"""

VGhpcyBpcyBhIHRlc3Qgc3RyaW5nIHRoYXQgd2FzIGVuY29kZWQgaW4gQmFzZTY0Lg==

ASCII : mike spon

Rot13 : zvxr fcba

Base64 : bWlrZSBzcG9u

Binary : 01101101 01101001 01101011 01100101 00100000 01110011 01110000 01101111 01101110
         011011010110100101101011011001010010000001110011011100000110111101101110

Hex : 6D 69 6B 65 20 73 70 6F 6E

Dec : 109 105 107 101 32 115 112 111 110
      10910510710132115112111110

Oct : 155 151 153 145 40 163 160 157 156

Morse Code : -- .. -.- .  ... .--. --- -.

"""