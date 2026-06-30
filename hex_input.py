# !/usr/bin/env python3

import base64
import functools

from results import Results
from morse_code import MorseCode


def handle_exceptions(func):
    """
    Defining the error handling decorator.
    """
    # Preserves the original function's name and docstring
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except AttributeError as e:
            return f"{e}"
        except TypeError as e:
            return f"[Error Handled] {hex_str} caused a TypeError in '{func.__name__}': {e}"
        except ValueError as e:
            hex_str = args[0] if args else "Unknown Input"
            return f"[Error Handled] {hex_str} caused a ValueError in '{func.__name__}': {e}"
        except UnicodeDecodeError:
            return f"[Error: This hex sequence ({hex_str}) contains binary data that cannot be read as text]"
        except Exception as e:
            return f"[Error Handled] An unexpected error occurred: {e}"
    return wrapper


class Hexadecimal:


    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def clean_hex_input(self) -> str:
        hex_str = self.input_string.strip().lower()
        hex_str = hex_str.replace(" ", "")
        if hex_str.startswith("0x"):
            hex_str = hex_str[2:]
        return hex_str


    @handle_exceptions
    def hex_to_ascii(self) -> str:
        """
        Converts a hexadecimal string to its representation in ascii
        characters.
        """
        # hex_str = self.clean_hex_input(input_string)
        # raw_bytes = bytes.fromhex(hex_str)
        # return raw_bytes.decode("utf-8")

        return bytes.fromhex(self.clean_hex_input(self.input_string)).decode("utf-8")


    @handle_exceptions
    def hex_to_base64(self) -> str:
        """
        Converts a hexadecimal string to its base64 representation.
        """
        hex_str = self.clean_hex_input(self.input_string)
        raw_bytes = bytes.fromhex(hex_str)
        return base64.b64encode(raw_bytes).decode("utf-8")


    @handle_exceptions
    def hex_to_binary(self) -> str:
        """
        Converts a hexadecimal string to its binary representation.
        """
        hex_str = self.clean_hex_input(self.input_string)
        return " ".join(f"{b:08b}" for b in bytes.fromhex(hex_str))


    @handle_exceptions
    def hex_to_decimal(self) -> str:
        """
        Converts a hex string to signed and unsigned representations.

        Args:
            hex_str (str): Hex string (e.g. 'FFFF', '0xFF').

        Returns:
            dict: Contains 'signed' and 'unsigned' representations.
        """
        hex_str = self.clean_hex_input(self.input_string)

        unsigned_value = int(hex_str, 16)
        bit_length = len(hex_str) * 4
        signed_value = unsigned_value

        if unsigned_value >= 2 ** (bit_length - 1):
            signed_value -= 2 ** bit_length

        decimal_results = {
            "Decimal (signed)": f"{signed_value:,}",
            "Decimal (unsigned)": f"{unsigned_value:,}"
        }

        return decimal_results


    @handle_exceptions
    def hex_to_morse_code(self) -> str:
        hex_str = self.clean_hex_input(self.input_string)
        return MorseCode.encode_morse_code(self, input_string=hex_str)


    @handle_exceptions
    def hex_convert_all(self) -> dict:
        self.results["type"] = "Hexadecimal"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Ascii"] = f"{self.hex_to_ascii()}"
        self.results["Base64"] = f"{self.hex_to_base64()}"
        self.results["Binary"] = f"{self.hex_to_binary()}"

        for key, value in self.hex_to_decimal(self.input_string).items():
            self.results[f"{key}"] = f"{value}"

        return self.results


    @handle_exceptions
    def print_hex_output(self) -> None:
        results_dict = self.hex_convert_all()
        Results.print_results_table(self, results_dict=results_dict)
