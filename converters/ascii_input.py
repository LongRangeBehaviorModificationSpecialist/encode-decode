# !/usr/bin/env python3

import base64
import codecs
from rich.console import Console
from rich.prompt import Prompt
from rich.traceback import install
import string
from typing import Dict, Tuple

from results import Results
from converters.morse_code import MorseCode


c = Console()
install(show_locals=True)


class Ascii:

    PRINTABLE_ASCII = set(string.printable)
    CONTROL_CHARS = set(chr(i) for i in range(32) if chr(i) not in '\t\n\r')
    WHITESPACE = set(string.whitespace)

    def __init__(self):
        self.morse_code = MorseCode()


    def validate_ascii_input(self, input: str) -> Tuple[bool, str]:
        """Comprehensive input validation."""
        if not input:
            return False, "Input cannot be empty"

        if not isinstance(input, str):
            return False, "Input must be a string"

        issues = []
        for pos, char in enumerate(input):
            code = ord(char)

            if code > 127:
                issues.append(f"Position {pos} -> Non-ASCII '{char}' (U+{code:04X})")
            elif char in self.CONTROL_CHARS:
                issues.append(f"Position {pos}: Control character (ord={code})")

        if issues:
            return False, "; ".join(issues[:3]) + ("..." if len(issues) > 3 else "")

        return True, ""



    def sanitize_input(self, input: str, mode: str = "strict") -> str:
        """Sanitize input based on mode.

        Args:
            mode: "strict" (raise), "replace" (swap bad chars), "remove"
                (delete bad chars)
        """
        sanitized = []

        for char in input:
            code = ord(char)

            # Valid ASCII
            if code <= 127:
                # Printable or safe whitespace
                if code >= 32 or char in '\t\n\r':
                    sanitized.append(char)
                elif mode == "remove":
                    # Skip control chars
                    continue
                elif mode == "replace":
                    # Replace control chars
                    sanitized.append('?')
                # Strict mode
                else:
                    raise ValueError(f"Control character at position: ord({code})")
            # Non-ASCII characters
            else:
                if mode == "remove":
                    continue
                elif mode == "replace":
                    sanitized.append('?')
                else:
                    raise ValueError(f"Non-ASCII character -> '{char}'")
        return ''.join(sanitized)


    def ascii_to_base64(self, input: str) -> str:
        """Convert the ascii input string to base64 string."""
        is_valid, error_msg = self.validate_ascii_input(input)
        if not is_valid:
            raise ValueError(error_msg)
        return base64.b64encode(input.encode("ascii", errors="ignore")).decode()


    def ascii_to_base32(self, input: str) -> str:
        """Converts an ascii string to its base32 encoded representation."""
        is_valid, error_msg = self.validate_ascii_input(input)
        if not is_valid:
            raise ValueError(error_msg)
        return base64.b32encode(input.encode("ascii", errors="ignore")).decode("ascii")


    def ascii_to_binary(self, input: str) -> str:
        """Convert the ascii input string to binary string."""
        is_valid, error_msg = self.validate_ascii_input(input)
        if not is_valid:
            raise ValueError(error_msg)
        return " ".join(bin(ord(c))[2:].zfill(8) for c in input)


    def ascii_to_decimal(self, input: str) -> str:
        """Convert the ascii input string to decimal string."""
        is_valid, error_msg = self.validate_ascii_input(input)
        if not is_valid:
            raise ValueError(error_msg)
        return " ".join(str(ord(i)) for i in input)


    def ascii_to_hexadecimal(self, input: str) -> str:
        """Convert the ascii input string to hexadecimal string."""
        is_valid, error_msg = self.validate_ascii_input(input)
        if not is_valid:
            raise ValueError(error_msg)
        return " ".join(f"{ord(c):02X}" for c in input)


    def ascii_to_rot13(self, input: str) -> str:
        """Convert the ascii input string to rot13 string."""
        is_valid, error_msg = self.validate_ascii_input(input)
        if not is_valid:
            raise ValueError(error_msg)
        return codecs.encode(input, "rot_13")


    def make_data_dict(self, input: str) -> Dict[str, str]:
        results = {}
        results["Input Type"] = "Ascii"
        results["Input Value"] = f"{input}"
        results["Validation OK"] = True
        try:
            results["Base64"] = f"{self.ascii_to_base64(input=input)}"
            results["Base32"] = f"{self.ascii_to_base32(input=input)}"
            results["Binary"] = f"{self.ascii_to_binary(input=input)}"
            results["Decimal"] = f"{self.ascii_to_decimal(input=input)}"
            results["Hexadecimal"] = f"{self.ascii_to_hexadecimal(input=input)}"
            results["Rot13"] = f"{self.ascii_to_rot13(input=input)}"
            results["Morse code"] = (
                f"{self.morse_code.encode_morse_code(input=input)}"
            )
        except ValueError as e:
            results["Validation OK"] = False
            results["error"] = str(e)
        return results


    def run_ascii_convert(self):
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        try:
            results = self.make_data_dict(input=input)
            Results.print_results_table(results_dict=results)
        except ValueError as e:
            c.print(f"[red1]Validation Error -> {e}")
            c.print("[dim]Tip: Try simpler characters like letters and numbers.")
