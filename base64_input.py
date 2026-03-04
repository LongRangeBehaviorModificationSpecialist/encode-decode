# !/usr/bin/env python3
# DLU : 04-Mar-2026

import base64

from results import Results
from morse_code import MorseCode


class Base64:


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

        results = {}
        results["type"] = "Base64"
        results["input"] = f"{input_string}"

        ascii = Base64.base64_to_ascii(self, input_string)
        results["ASCII"] = f"{ascii}"

        binary = Base64.base64_to_binary(self, input_string)
        results["Binary"] = f"{binary}"

        decimal = Base64.base64_to_decimal(self, input_string)
        results["Decimal"] = f"{decimal}"

        hex = Base64.base64_to_hexadecimal(self, input_string)
        results["Hexadecimal"] = f"{hex}"

        morse_code = MorseCode.encode_morse_code(self, input_string)
        results["Morse Code"] = f"{morse_code}"

        return results


    def print_base64_output(self, input_string: str) -> None:
        results = Base64.make_data_dict(self, input_string)
        Results.print_results_table(self, results_dict=results)
