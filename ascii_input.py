# !/usr/bin/env python3
# DLU : 04-Mar-2026

import base64
import codecs

from results import Results
from morse_code import MorseCode


class ASCII:


    def __init__(self, results, data_type):
        self.results = results
        self.data_type = data_type


    def ascii_to_base64(self, input_string: str) -> str:
        """Convert the ASCII input string to BASE64 string."""
        b64_string = base64.b64encode(input_string.encode()).decode()
        return b64_string


    def ascii_to_binary(self, input_string: str) -> str:
        """Convert the ASCII input string to BINARY string."""
        b = ""
        for c in input_string:
            b += bin(ord(c))[2:].zfill(8)
        s = [b[i:i+8] for i in range(0, len(b), 8)]
        binary_string = " ".join(x for x in s)
        return binary_string


    def ascii_to_decimal(self, input_string: str) -> str:
        """Convert the ASCII input string to DECIMAL string."""
        decimal_string = " ".join(
            str(x) for x in [ord(i) for i in input_string])
        return decimal_string


    def ascii_to_hexadecimal(self, input_string: str) -> str:
        """Convert the ASCII input string to HEXADECIMAL string."""
        hex_string = " ".join(f"{ord(c):02X}" for c in input_string)
        return hex_string


    def ascii_to_rot13(self, input_string: str) -> str:
        """Convert the ASCII input string to ROT13 string."""
        rot13_string = codecs.encode(input_string, "rot_13")
        return rot13_string


    def make_data_dict(self, input_string: str) -> dict:
        self.results["type"] = "ascii"
        self.results["user_input"] = f"{input_string}"
        self.results["Base64"] = f"{self.ascii_to_base64(input_string)}"
        self.results["Binary"] = f"{self.ascii_to_binary(input_string)}"
        self.results["Decimal"] = f"{self.ascii_to_decimal(input_string)}"
        self.results["Hexadecimal"] = f"{self.ascii_to_hexadecimal(input_string)}"
        self.results["Rot13"] = f"{self.ascii_to_rot13(input_string)}"
        self.results["Morse Code"] = f"{MorseCode.encode_morse_code(self, input_string)}"
        return self.results


    def print_ascii_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    format=self.data_type,
                                    results_dict=output)