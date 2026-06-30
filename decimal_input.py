# !/usr/bin/env python3

import base64

from rich.console import Console
from rich.traceback import install

from results import Results


c = Console()
install()


class DecimalInteger:


    def __init__(self, input_string: str, results: dict):
        parsed_string = input_string.replace(",", "")
        self.number = int(parsed_string)
        self.results = results


    def format_input(self):
        if "," in self.input_string:
            self.input_string = self.input_string.replace(",", "")
        return int(self.input_string)


    def decimal_to_binary(self) -> str:
        """
        Convert the decimal number to binary number.
        """
        return "{0:b}".format(self.number)


    def decimal_to_hexadecimal(self) -> str:
        """
        Convert the decimal number to hexadecimal number.
        """
        hex_str = hex(self.number)[2:]
        if len(hex_str) % 2 != 0:
            hex_str = "0" + hex_str
        pairs = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
        return "0x " + " ".join(pairs).upper()


    def decimal_to_octal(self) -> str:
        """
        Convert the decimal number to octal number.
        """
        return oct(self.number)


    def make_data_dict(self) -> None:
        self.results["type"] = "Decimal (integer)"
        self.results["user_input"] = f"{self.number}"
        self.results["Binary"] = f"{self.decimal_to_binary()}"
        self.results["Hexadecimal"] = f"{self.decimal_to_hexadecimal()}"
        self.results["Octal"] = f"{self.decimal_to_octal()}"
        return self.results


    def print_decimal_integer_output(self) -> None:
        results_dict = self.make_data_dict()
        Results.print_results_table(self, results_dict=results_dict)


class DecimalString:

    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def decimal_to_ascii(self) -> str:
        try:
            return "".join(chr(int(c)) for c in self.input_string.split())

        except ValueError:
            c.print("[bold bright_red]Error: Please ensure the input only \
contains numbers separated by spaces.")
        except OverflowError:
            c.print("[bold bright_red]Error: One of the numbers is too large \
to be a valid ascii character.")


    def decimal_to_base64(self) -> str:
        byte_data = bytes(int(c) for c in self.input_string.split())
        return base64.b64encode(byte_data).decode("utf-8")


    def make_data_dict(self) -> None:
        self.results["type"] = "Decimal (String)"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Ascii"] = f"{self.decimal_to_ascii()}"
        self.results["Base64"] = f"{self.decimal_to_base64()}"
        return self.results


    def print_decimal_string_output(self) -> None:
        results_dict = self.make_data_dict()
        Results.print_results_table(self, results_dict=results_dict)
