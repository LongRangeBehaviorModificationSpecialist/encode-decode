# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from rich.console import Console

from results import Results

# Make the console object
console = Console()


class Octal:


    def octal_to_binary(self, input_num: int) -> int:
        """Converts an octal string to binary.

        Args:
          input_num: An octal number.

        Returns:
          The binary equivalent of the octal number.
        """
        binary_number = bin(int(str(input_num), 8))
        return binary_number[2:]


    def octal_to_decimal(self, input_num: int) -> int:
        """Converts an octal string to a decimal integer.

        Args:
          input_num: An octal number.

        Returns:
          The decimal equivalent of the octal number.
        """
        decimal_num = 0
        for digit in input_num:
            decimal_num = (decimal_num * 8) + int(digit)
        return decimal_num


    def octal_to_hexadecimal(self, input_num: int) -> int:
        """Converts an octal string to hexadecimal.

        Args:
          input_num: The octal number.

        Returns:
          The hexadecimal representation of the octal number.
        """
        hex_number = hex(int(input_num, 8))[2:].upper()
        return hex_number


    def octal_convert_all(self, input_num: str) -> dict:

        octal_results_dict = {}

        octal_results_dict['type'] = 'Octal'
        octal_results_dict['input'] = f'{input_num}'
        binary = Octal.octal_to_binary(self, input_num)
        octal_results_dict['Binary'] = f'{binary}'
        decimal = Octal.octal_to_decimal(self, input_num)
        octal_results_dict['Decimal'] = f'{decimal}'
        hexadecimal = Octal.octal_to_hexadecimal(self, input_num)
        octal_results_dict['Hexadecimal'] = f'{hexadecimal}'

        return octal_results_dict


    def print_octal_output_panels(self, input_string: str) -> None:
        octal_results_dict = Octal.octal_convert_all(
            self, input_string=input_string
        )
        Results.print_results_panels(
            self, results_dict=octal_results_dict
        )


    def print_octal_output_table(self, input_string: str) -> None:
        octal_results_dict = Octal.octal_convert_all(
            self, input_string=input_string
        )
        Results.print_results_table(
            self, results_dict=octal_results_dict
        )
