# !/usr/bin/env python3

import base64

from results import Results
from morse_code import MorseCode


class Base64:


    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def base64_to_ascii(self) -> str:
        """
        Convert base64 string to ascii string.
        """
        return base64.b64decode(self.input_string).decode()


    def base64_to_base32(self) -> str:
        """
        Convert a base64 string to a base32 string.
        """
        raw_bytes = base64.b64decode(self.input_string)
        return base64.b32encode(raw_bytes).decode("ascii")


    def base64_to_binary(self) -> str:
        """
        Convert base64 string to binary string.
        """
        return " ".join(
            format(ord(c), "b").zfill(8) for c in base64.b64decode(
                self.input_string).decode())


    def base64_to_decimal(self) -> str:
        """
        Convert base64 string to decimal string.
        """
        d = [ord(c) for c in base64.b64decode(self.input_string).decode()]
        return " ".join(str(x) for x in d)


    def base64_to_hexadecimal(self) -> str:
        """
        Convert base64 string to hexadecimal string.
        """
        decoded_bytes = base64.b64decode(self.input_string)
        return " ".join(f"{n:02x}" for n in decoded_bytes).upper()


    def make_data_dict(self) -> None:
        self.results["type"] = "Base64"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Ascii"] = f"{self.base64_to_ascii()}"
        self.results["Base32"] = f"{self.base64_to_base32()}"
        self.results["Binary"] = f"{self.base64_to_binary()}"
        self.results["Decimal"] = f"{self.base64_to_decimal()}"
        self.results["Hexadecimal"] = f"{self.base64_to_hexadecimal()}"
        self.results["Morse Code"] = f"{MorseCode.encode_morse_code(self, self.input_string)}"
        return self.results


    def print_base64_output(self) -> None:
        results_dict = self.make_data_dict()
        Results.print_results_table(self, results_dict=results_dict)
