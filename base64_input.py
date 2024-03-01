# !/usr/bin/env python3

import base64
from rich.console import Console

from results import Results
from morse_code import MorseCode

# Make the console object
console = Console()


class Base64:


    def base64_to_ascii(self, input_string: str) -> str:
        '''Convert BASE64 string to ASCII string.'''
        ascii_string = base64.b64decode(input_string).decode()
        return ascii_string


    def base64_to_binary(self, input_string: str) -> str:
        '''Convert BASE64 string to BINARY string.'''
        binary_string = ' '.join(
            format(ord(i), 'b').zfill(8) for i in base64.b64decode(
                input_string).decode())
        return binary_string


    def base64_to_decimal(self, input_string: str) -> str:
        '''Convert BASE64 string to DECIMAL string.'''
        d = [ord(i) for i in base64.b64decode(input_string).decode()]
        dec_result = ' '.join(str(x) for x in d)
        return dec_result


    def base64_to_hexadecimal(self, input_string: str) -> str:
        '''Convert BASE64 string to HEXADECIMAL string.'''
        hex_result = base64.b64decode(input_string).hex()
        return hex_result.upper()


    def base64_to_octal(self, input_string: str) -> str:
        octal_string = ''
        for char in input_string:
            octal_string += oct(ord(char))[2:]
        return octal_string


    def base64_convert_all(self, input_string: str) -> None:

        results = {}

        results['type'] = 'Base64'

        results['input'] = f'{input_string}'

        ascii = Base64.base64_to_ascii(
            self,
            input_string)
        results['ASCII'] = f'{ascii}'

        binary = Base64.base64_to_binary(
            self,
            input_string)
        results['Binary'] = f'{binary}'

        decimal = Base64.base64_to_decimal(
            self,
            input_string)
        results['Decimal'] = f'{decimal}'

        hex = Base64.base64_to_hexadecimal(
            self,
            input_string)
        results['Hexadecimal'] = f'{hex}'

        octal = Base64.base64_to_octal(
            self,
            input_string)
        results['Octal'] = f'{octal}'

        morse_code = MorseCode.encode_morse_code(
            self,
            input_string)
        results['Morse Code'] = f'{morse_code}'

        return results


    def print_base64_output_panels(self, input_string: str) -> None:
        results = Base64.base64_convert_all(
            self,
            input_string=input_string)

        Results.print_results_panels(
            self,
            results_dict=results)


    def print_ascii_output_table(self, input_string: str) -> None:
        results = Base64.base64_convert_all(
            self,
            input_string=input_string)

        Results.print_results_table(
            self,
            results_dict=results)
