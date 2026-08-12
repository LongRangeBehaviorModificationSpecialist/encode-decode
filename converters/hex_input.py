# !/usr/bin/env python3

import base64
import functools
from rich.prompt import Prompt
from rich.traceback import install
from results import Results
from converters.morse_code import MorseCode


install(show_locals=True)


def handle_exceptions(func):
    """Defining the error handling decorator."""
    # Preserves the original function's name and docstring
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except AttributeError as e:
            return f"{e}"
        except TypeError as e:
            return (
                f"[Error Handled] {hex_str} caused a TypeError in "
                f"'{func.__name__}' -> {e}."
            )
        except ValueError as e:
            hex_str = args[0] if args else "Unknown Input"
            return (
                f"[Error Handled] {hex_str} caused a ValueError in "
                f"{func.__name__}' -> {e}."
            )
        except UnicodeDecodeError:
            return (
                f"Error: This hex sequence ({hex_str}) contains binary data "
                "that cannot be read as text."
            )
        except Exception as e:
            return f"[Error Handled] An unexpected error occurred -> {e}"
    return wrapper


class Hexadecimal:


    def clean_hex_input(self, input: str) -> str:
        hex_str = input.strip().lower()
        hex_str = hex_str.replace(" ", "")
        if hex_str.startswith("0x"):
            hex_str = hex_str[2:]
        return hex_str


    @handle_exceptions
    def hex_to_ascii(self, input: str) -> str:
        """Converts a hexadecimal string to its representation in ascii
        characters.
        """
        return bytes.fromhex(
            self.clean_hex_input(input)).decode("utf-8")


    @handle_exceptions
    def hex_to_base64(self, input: str) -> str:
        """Converts a hexadecimal string to its base64 representation."""
        hex_str = self.clean_hex_input(input)
        raw_bytes = bytes.fromhex(hex_str)
        return base64.b64encode(raw_bytes).decode("utf-8")


    @handle_exceptions
    def hex_to_binary(self, input: str) -> str:
        """Converts a hexadecimal string to its binary representation."""
        hex_str = self.clean_hex_input(self.input_string)
        return " ".join(f"{b:08b}" for b in bytes.fromhex(hex_str))


    @handle_exceptions
    def hex_to_decimal(self, input: str) -> str:
        """Converts a hex string to signed and unsigned representations.

        Args:
            hex_str (str): Hex string (e.g. 'FFFF', '0xFF').

        Returns:
            dict: Contains 'signed' and 'unsigned' representations.
        """
        hex_str = self.clean_hex_input(input)

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
    def hex_to_morse_code(self, input: str) -> str:
        hex_str = self.clean_hex_input(input)
        return MorseCode.encode_morse_code(self, input=hex_str)


    @handle_exceptions
    def make_data_dict(self, input: str) -> dict:
        results = {}
        results["Input Type"] = "Hexadecimal"
        results["Input Value"] = f"{input}"
        results["ascii"] = f"{self.hex_to_ascii(input=input)}"
        results["base64"] = f"{self.hex_to_base64(input=input)}"
        results["binary"] = f"{self.hex_to_binary(input=input)}"

        for key, value in self.hex_to_decimal(input).items():
            results[f"{key}"] = f"{value}"

        return results


    @handle_exceptions
    def run_hex_convert(self) -> None:
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        results = self.make_data_dict(input=input)
        Results.print_results_table(self, results_dict=results)
