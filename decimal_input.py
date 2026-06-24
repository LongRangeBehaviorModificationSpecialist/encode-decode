# !/usr/bin/env python3
# DLU : 24-Jun-2026

import base64

from rich.console import Console
from rich.traceback import install

from results import Results


c = Console()
install()

class DecimalInteger:


    def __init__(self, data_type, results):
        self.data_type = data_type
        self.results = results


    def decimal_to_binary(self, input_string: int) -> str:
        """Convert the DECIMAL number string to BINARY number."""
        binary_string = "{0:b}".format(int(input_string))
        return binary_string


    def decimal_to_hexadecimal(self, input_string: int) -> str:
        """Convert the DECIMAL number string to HEXADECIMAL number."""
        hex_string = hex(int(input_string))
        return hex_string


    def decimal_to_octal(self, input_string: int) -> str:
        """Convert the DECIMAL number string to OCTAL number."""
        octal_string = oct(int(input_string))
        return octal_string


    def make_data_dict(self, input_string: int) -> None:
        self.results["type"] = "Decimal (Integer)"
        self.results["user_input"] = f"{input_string}"
        self.results["Binary"] = f"{self.decimal_to_binary(input_string)}"
        self.results["Hexadecimal"] = f"{self.decimal_to_hexadecimal(input_string)}"
        self.results["Octal"] = f"{self.decimal_to_octal(input_string)}"
        return self.results


    def print_decimal_integer_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    format=self.data_type,
                                    results_dict=output)


class DecimalString:

    def __init__(self, results, data_type):
        self.results = results
        self.data_type = data_type


    def decimal_to_ascii(self, input_string: int) -> str:
        try:
            ascii_string = "".join(chr(int(c)) for c in input_string.split())
            return ascii_string

        except ValueError:
            c.print("[bold bright_red]Error: Please ensure the input only \
contains numbers separated by spaces.")
        except OverflowError:
            c.print("[bold bright_red]Error: One of the numbers is too large \
to be a valid ascii character.")


    def decimal_to_base64(self, input_string: str) -> str:
        byte_data = bytes(int(c) for c in input_string.split())
        base64_string = base64.b64encode(byte_data).decode("utf-8")
        return base64_string


    def make_data_dict(self, input_string: int) -> None:
        self.results["type"] = "Decimal (String)"
        self.results["user_input"] = f"{input_string}"
        self.results["ASCII"] = f"{self.decimal_to_ascii(input_string)}"
        self.results["Base64"] = f"{self.decimal_to_base64(input_string)}"
        return self.results


    def print_decimal_string_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    data_type=self.data_type,
                                    results_dict=output)
