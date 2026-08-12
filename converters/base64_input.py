# !/usr/bin/env python3

import base64
from rich.traceback import install
from rich.prompt import Prompt
from results import Results
from converters.morse_code import MorseCode


install(show_locals=True)


class Base64:


    def base64_to_ascii(self, input: str) -> str:
        """Convert base64 string to ascii string."""
        return base64.b64decode(input).decode()


    def base64_to_base32(self, input: str) -> str:
        """Convert a base64 string to a base32 string."""
        raw_bytes = base64.b64decode(input)
        return base64.b32encode(raw_bytes).decode("ascii")


    def base64_to_binary(self, input: str) -> str:
        """Convert base64 string to binary string."""
        return " ".join(
            format(ord(c), "b").zfill(8) for c in base64.b64decode(
                input).decode()
        )


    def base64_to_decimal(self, input: str) -> str:
        """Convert base64 string to decimal string."""
        d = [ord(c) for c in base64.b64decode(input).decode()]
        return " ".join(str(x) for x in d)


    def base64_to_hexadecimal(self, input: str) -> str:
        """Convert base64 string to hexadecimal string."""
        decoded_bytes = base64.b64decode(input)
        return " ".join(f"{n:02x}" for n in decoded_bytes).upper()


    def make_data_dict(self, input: str) -> None:
        results = {}
        results["Input Type"] = "Base64"
        results["Input Value"] = f"{input}"
        results["ascii"] = f"{self.base64_to_ascii(input=input)}"
        results["base32"] = f"{self.base64_to_base32(input=input)}"
        results["binary"] = f"{self.base64_to_binary(input=input)}"
        results["decimal"] = f"{self.base64_to_decimal(input=input)}"
        results["hexadecimal"] = f"{self.base64_to_hexadecimal(input=input)}"
        results["morse code"] = (
            f"{MorseCode.encode_morse_code(self, input=input)}"
        )
        return results


    def run_base64_convert(self):
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        results = self.make_data_dict(input=input)
        Results.print_results_table(self, results_dict=results)
