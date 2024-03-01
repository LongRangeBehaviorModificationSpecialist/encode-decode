# !/usr/bin/env python3

import base64
import codecs
from rich.console import Console

from results import Results
from morse_code import MorseCode

# Make the console object
console = Console()


class ASCII:


    def ascii_to_base64(self, input_string: str) -> str:
        '''Convert the ASCII input string to BASE64 string.'''
        b64_string = base64.b64encode(input_string.encode()).decode()
        return b64_string


    def ascii_to_binary(self, input_string: str) -> str:
        '''Convert the ASCII input string to BINARY string.'''
        b = ''
        for c in input_string:
            b += bin(ord(c))[2:].zfill(8)
        s = [b[i:i+8] for i in range(0, len(b), 8)]
        binary_string = ' '.join(x for x in s)
        return binary_string


    def ascii_to_decimal(self, input_string: str) -> str:
        '''Convert the ASCII input string to DECIMAL string.'''
        decimal_string = ' '.join(
            str(x) for x in [ord(i) for i in input_string])
        return decimal_string


    def ascii_to_hexadecimal(self, input_string: str) -> str:
        '''Convert the ASCII input string to HEXADECIMAL string.'''
        hex_string = ''
        for c in input_string:
            hex_string += hex(ord(c))[2:]
        return hex_string.upper()


    def ascii_to_octal(self, input_string: str) -> str:
        '''Convert the ASCII input string to OCTAL string.'''
        octal_string = ''
        for char in input_string:
            octal_string += f'{oct(ord(char))[2:]} '
        return octal_string


    def ascii_to_rot13(self, input_string: str) -> str:
        '''Convert the ASCII input string to ROT13 string.'''
        rot13_string = codecs.encode(input_string, 'rot_13')
        return rot13_string


    def ascii_convert_all(self, input_string: str) -> dict:

        results = {}
        results['type'] = 'ascii'
        results['input'] = f'{input_string}'

        b64 = ASCII.ascii_to_base64(self, input_string)
        results['Base64'] = f'{b64}'

        binary = ASCII.ascii_to_binary(self, input_string)
        results['Binary'] = f'{binary}'

        decimal = ASCII.ascii_to_decimal(self, input_string)
        results['Decimal'] = f'{decimal}'

        hex = ASCII.ascii_to_hexadecimal(self, input_string)
        results['Hexadecimal'] = f'{hex}'

        octal = ASCII.ascii_to_octal(self, input_string)
        results['Octal'] = f'{octal}'

        rot13 = ASCII.ascii_to_rot13(self, input_string)
        results['Rot13'] = f'{rot13}'

        morse_code = MorseCode.encode_morse_code(self, input_string)
        results['Morse Code'] = f'{morse_code}'

        return results


    def print_ascii_output_panels(self, input_string: str) -> None:
        results = ASCII.ascii_convert_all(self, input_string)
        Results.print_results_panels(self, results_dict=results)


    def print_ascii_output_table(self, input_string: str) -> None:
        results = ASCII.ascii_convert_all(self, input_string)
        Results.print_results_table(self, results_dict=results)