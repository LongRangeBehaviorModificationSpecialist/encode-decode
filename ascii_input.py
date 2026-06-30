# !/usr/bin/env python3

import base64
import codecs

from results import Results
from morse_code import MorseCode


class Ascii:


    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def ascii_to_base64(self) -> str:
        """
        Convert the ascii input string to base64 string.
        """
        return base64.b64encode(self.input_string.encode()).decode()


    def ascii_to_base32(self) -> str:
        """
        Converts an ascii string to its base32 encoded representation.
        """
        return base64.b32encode(self.input_string.encode()).decode("ascii")


    def ascii_to_binary(self) -> str:
        """
        Convert the ascii input string to binary string.
        """
        b = ""
        for c in self.input_string:
            b += bin(ord(c))[2:].zfill(8)
        s = [b[i:i+8] for i in range(0, len(b), 8)]
        return " ".join(x for x in s)


    def ascii_to_decimal(self) -> str:
        """
        Convert the ascii input string to decimal string.
        """
        return " ".join(str(x) for x in [ord(i) for i in self.input_string])


    def ascii_to_hexadecimal(self) -> str:
        """
        Convert the ascii input string to hexadecimal string.
        """
        return " ".join(f"{ord(c):02X}" for c in self.input_string)


    def ascii_to_rot13(self) -> str:
        """
        Convert the ascii input string to rot13 string.
        """
        return codecs.encode(self.input_string, "rot_13")


    def make_data_dict(self) -> dict:
        self.results["type"] = "Ascii"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Base64"] = f"{self.ascii_to_base64()}"
        self.results["Base32"] = f"{self.ascii_to_base32()}"
        self.results["Binary"] = f"{self.ascii_to_binary()}"
        self.results["Decimal"] = f"{self.ascii_to_decimal()}"
        self.results["Hexadecimal"] = f"{self.ascii_to_hexadecimal()}"
        self.results["Rot13"] = f"{self.ascii_to_rot13()}"
        self.results["Morse Code"] = f"{MorseCode.encode_morse_code(self, self.input_string)}"
        return self.results


    def print_ascii_output(self) -> None:
        results_dict = self.make_data_dict()
        Results.print_results_table(self, results_dict=results_dict)