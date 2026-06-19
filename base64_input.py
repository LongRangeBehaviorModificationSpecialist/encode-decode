# !/usr/bin/env python3

import base64

from results import Results
from morse_code import MorseCode


class Base64:

    def __init__(self, results, data_type):
        self.results = results
        self.data_type = data_type


    def base64_to_ascii(self, input_string: str) -> str:
        """Convert BASE64 string to ASCII string."""
        ascii_string = base64.b64decode(input_string).decode()
        return ascii_string


    def base64_to_binary(self, input_string: str) -> str:
        """Convert BASE64 string to BINARY string."""
        binary_string = " ".join(
            format(ord(i), "b").zfill(8) for i in base64.b64decode(
                input_string).decode())
        return binary_string


    def base64_to_decimal(self, input_string: str) -> str:
        """Convert BASE64 string to DECIMAL string."""
        d = [ord(i) for i in base64.b64decode(input_string).decode()]
        dec_result = " ".join(str(x) for x in d)
        return dec_result


    def base64_to_hexadecimal(self, input_string: str) -> str:
        """Convert BASE64 string to HEXADECIMAL string."""
        decoded_bytes = base64.b64decode(input_string)
        spaced_result = " ".join(f"{n:02x}" for n in decoded_bytes)
        return spaced_result.upper()


    def make_data_dict(self, input_string: str) -> None:
        self.results["type"] = "Base64"
        self.results["user_input"] = f"{input_string}"
        ascii = self.base64_to_ascii(input_string)
        self.results["ASCII"] = f"{ascii}"
        binary = self.base64_to_binary(input_string)
        self.results["Binary"] = f"{binary}"
        decimal = self.base64_to_decimal(input_string)
        self.results["Decimal"] = f"{decimal}"
        hex = self.base64_to_hexadecimal(input_string)
        self.results["Hexadecimal"] = f"{hex}"
        morse_code = MorseCode.encode_morse_code(self, input_string)
        self.results["Morse Code"] = f"{morse_code}"
        return self.results


    def print_base64_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    format=self.data_type,
                                    results_dict=output)
