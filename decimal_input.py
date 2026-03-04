# !/usr/bin/env python3
# DLU : 04-Mar-2026

import base64

from results import Results


class Decimal:

    # def decimal_to_ascii(self, input_string: int) -> str:
    #     """Converts a sequence of decimal ASCII codes to a string."""

    #     if not isinstance(input_string, str):
    #         raise TypeError("Input must be a string.")

    #     decimal_sequence = input_string.strip()

    #     if not decimal_sequence:
    #         raise ValueError("Input cannot be empty.")

    #     # Split by spaces and convert each decimal to integer
    #     try:
    #         numbers = [int(num) for num in decimal_sequence.split()]
    #     except ValueError:
    #         raise ValueError("Input must be space-separated decimal numbers.")

    #     # Convert each number to ASCII character then join into a single string
    #     ascii_result = "".join([chr(num) for num in numbers])

    #     return ascii_result


        # input_list = []
        # input_parts = input_string.split(" ")
        # for i in input_parts:
        #     input_list.append(int(i))
        # ascii_result = "".join(chr(x) for x in input_list)
        # return ascii_result


    # def decimal_to_base64(self, input_string: int) -> str:
    #     """Convert the DECIMAL input string to BASE64 string."""
    #     ascii_string = Decimal.decimal_to_ascii(self, input_string)
    #     b64_string = base64.b64encode(str(ascii_string).encode()).decode()
    #     return b64_string


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

        results = {}
        results["type"] = "Decimal"
        results["input"] = f"{input_string}"

        # ascii = Decimal.decimal_to_ascii(self, input_string)
        # results["ASCII"] = f"{ascii}"

        # base64 = Decimal.decimal_to_base64(self, input_string)
        # results["Decimal -> ASCII -> Base64"] = f"{base64}"

        binary = Decimal.decimal_to_binary(self, input_string)
        results["Binary"] = f"{binary}"

        hex = Decimal.decimal_to_hexadecimal(self, input_string)
        results["Hexadecimal"] = f"{hex}"

        octal = Decimal.decimal_to_octal(self, input_string)
        results["Octal"] = f"{octal}"

        return results


    def print_decimal_output(self, input_string: str) -> None:
        results = Decimal.make_data_dict(self, input_string)
        Results.print_results_table(self,
                                    format="Decimal",
                                    results_dict=results)
