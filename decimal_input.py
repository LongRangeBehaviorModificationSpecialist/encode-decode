# !/usr/bin/env python3

import base64
from rich.console import Console

from results import Results

# Make the console object
console = Console()


class Decimal:


    def decimal_to_ascii(self, input_string: str) -> str:
        '''Convert the DECIMAL input string to ASCII string.'''
        input_list = []
        input_parts = input_string.split(' ')
        for i in input_parts:
            input_list.append(int(i))
        ascii_result = ''.join(chr(x) for x in input_list)
        return ascii_result


    def decimal_to_base64(self, input_string: str) -> str:
        '''Convert the DECIMAL input string to BASE64 string.'''
        ascii_string = Decimal.decimal_to_ascii(self, input_string)
        b64_string = base64.b64encode(str(ascii_string).encode()).decode()
        return b64_string


    def decimal_to_binary(self, input_string: str) -> str:
        '''Convert the DECIMAL input string to BINARY string.'''
        list_of_nums = input_string.split()
        binary_string = ' '.join([bin(int(x))[2:].zfill(8) for x in list_of_nums])
        return binary_string


    def decimal_to_hexadecimal(self, input_string: str) -> str:
        '''Convert the DECIMAL input string to HEXADECIMAL string.'''
        list_of_nums = input_string.split()
        hex_string = ''.join([hex(int(x))[2:] for x in list_of_nums]).upper()
        return hex_string.upper()


    def decimal_to_octal(self, input_string: str) -> str:
        '''Convert the DECIMAL input string to OCTAL string.'''
        octal_string = ''
        while input_string > 0:
            octal = str(input_string % 8) + octal
            input_string = input_string // 8
        return octal_string


    def decimal_convert_all(self, input_string: str) -> None:

        results = {}

        results['type'] = 'Decimal'

        results['input'] = f'{input_string}'

        ascii = Decimal.decimal_to_ascii(
            self,
            input_string)
        results['ASCII'] = f'{ascii}'

        base64 = Decimal.decimal_to_base64(
            self,
            input_string)
        results['Base64'] = f'{base64}'

        binary = Decimal.decimal_to_binary(
            self,
            input_string)
        results['Binary'] = f'{binary}'

        hex = Decimal.decimal_to_hexadecimal(
            self,
            input_string)
        results['Hexadecimal'] = f'{hex}'

        octal = Decimal.decimal_to_octal(
            self,
            input_string)
        results['Octal'] = f'{octal}'

        return results


    def print_decimal_output_panels(self, input_string: str) -> None:
        results = Decimal.decimal_convert_all(
            self,
            input_string=input_string)

        Results.print_results_panels(
            self,
            results_dict=results)


    def print_decimal_output_table(self, input_string: str) -> None:
        results = Decimal.decimal_convert_all(
            self,
            input_string=input_string)

        Results.print_results_table(
            self,
            results_dict=results)
