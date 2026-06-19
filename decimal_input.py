# !/usr/bin/env python3
# DLU : 04-Mar-2026

import base64

from results import Results


class Decimal:


    def __init__(self, results, data_type):
        self.results = results
        self.data_type = data_type


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
        self.results["type"] = "Decimal"
        self.results["user_input"] = f"{input_string}"
        # ascii = Decimal.decimal_to_ascii(self, input_string)
        # results["ASCII"] = f"{ascii}"
        # base64 = Decimal.decimal_to_base64(self, input_string)
        # results["Decimal -> ASCII -> Base64"] = f"{base64}"
        binary = self.decimal_to_binary(input_string)
        self.results["Binary"] = f"{binary}"
        hex = self.decimal_to_hexadecimal(input_string)
        self.results["Hexadecimal"] = f"{hex}"
        octal = self.decimal_to_octal(input_string)
        self.results["Octal"] = f"{octal}"
        return self.results


    def print_decimal_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    format=self.data_type,
                                    results_dict=output)
