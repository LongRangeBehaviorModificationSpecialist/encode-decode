# !/usr/bin/env python3

import binascii

from results import Results
from morse_code import MorseCode


class Hexadecimal:

    def hex_to_ascii(self, input_string: str) -> str:
        hex_string = input_string.replace(' ', '')
        string = binascii.unhexlify(hex_string)
        ascii_string = string.decode()
        return ascii_string


    def hex_to_base64(self, input_string: str) -> str:
        hex_string = input_string.replace(' ', '')
        hex_bytes = binascii.unhexlify(hex_string)
        base64_string = binascii.b2a_base64(hex_bytes).decode()
        return base64_string


    def hex_to_binary(self, input_string: str) -> str:
        ascii_string = Hexadecimal.hex_to_ascii(self, input_string)
        n = [x for x in ascii_string]
        binary_string = ' '.join([bin(ord(x))[2:].zfill(8) for x in n])
        return binary_string


    def hex_to_decimal(self, input_string: str) -> str:
        # Remove any spaces if present
        hex_string = input_string.replace(' ', '')
        # First, convert the HEX string to ASCII string
        ascii_string = binascii.unhexlify(hex_string)
        s = ascii_string.decode()
        # Conversion to DECIMAL string from ASCII
        d = [ord(i) for i in s]
        decimal_string = ' '.join(str(x) for x in d)
        return decimal_string


    def hex_to_morse_code(self, input_string: str) -> str:
        hex_string = input_string.replace(' ', '')
        morse_code_string = MorseCode.encode_morse_code(self,
            input_string=hex_string)
        return morse_code_string


    def hex_convert_all(self, input_string: str) -> None:

        results = {}
        results['type'] = 'Hexadecimal'
        results['input'] = f'{input_string}'

        ascii = Hexadecimal.hex_to_ascii(self, input_string)
        results['ASCII'] = f'{ascii}'

        base64 = Hexadecimal.hex_to_base64(self, input_string)
        results['Base64'] = f'{base64}'

        binary = Hexadecimal.hex_to_binary(self, input_string)
        results['Binary'] = f'{binary}'

        decimal = Hexadecimal.hex_to_decimal(self, input_string)
        results['Decimal'] = f'{decimal}'

        morse_code = Hexadecimal.hex_to_morse_code(self, input_string)
        results['Morse Code'] = f'{morse_code}'

        return results


    def print_hex_output_panels(self,
                                input_string: str) -> None:
        results = Hexadecimal.hex_convert_all(self, input_string)
        Results.print_results_panel(self, results_dict=results)


    def print_hex_output_table(self,
                               input_string: str) -> None:
        results = Hexadecimal.hex_convert_all(self, input_string)
        Results.print_results_table(self, results_dict=results)
