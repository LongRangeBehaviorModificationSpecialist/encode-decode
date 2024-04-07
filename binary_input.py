# !/usr/bin/env python3

import base64
from results import Results


class Binary:

    def binary_separated_to_ascii(self, input_string: str) -> str:
        # Convert the binary string to a list of integers.
        input_string = input_string.split()
        # Convert each integer to its ASCII character.
        integers = [int(x, 2) for x in input_string]
        c = [chr(i) for i in integers]
        # Join the ASCII characters into a string.
        ascii_separated_string = ''.join(c)
        return ascii_separated_string


    def binary_combined_to_ascii(self, input_string: str) -> str:
        list = []
        for i in range(0, len(input_string), 8):
            list.append(input_string[i:i+8])
        ascii_combined_string = ''.join([chr(int(i, 2)) for i in list])
        return ascii_combined_string


    def binary_separated_to_base64(self, input_string: str) -> str:
        ascii_result = Binary.binary_separated_to_ascii(self, input_string)
        ascii_to_b64 = ascii_result.encode('ascii')
        base64_bytes = base64.b64encode(ascii_to_b64)
        b64_result = base64_bytes.decode('ascii')
        return b64_result


    def binary_combined_to_base64(self, input_string: str) -> str:
        ascii_result = Binary.binary_combined_to_ascii(self, input_string)
        ascii_to_b64 = ascii_result.encode('ascii')
        base64_bytes = base64.b64encode(ascii_to_b64)
        b64_combined_result = base64_bytes.decode('ascii')
        return b64_combined_result


    def binary_separated_to_dec(self, input_string: str) -> str:
        ascii_result = Binary.binary_separated_to_ascii(self, input_string)
        d = [ord(i) for i in ascii_result]
        decimal_result = ' '.join(str(x) for x in d)
        return decimal_result


    def binary_combined_to_dec(self, input_string: str) -> str:
        ascii_result = Binary.binary_combined_to_ascii(self, input_string)
        d = [ord(i) for i in ascii_result]
        decimal_combined_result = ' '.join(str(x) for x in d)
        return decimal_combined_result


    def binary_separated_to_hex(self, input_string: str) -> str:
        ascii_result = Binary.binary_separated_to_ascii(self, input_string)
        hex_string = ''
        for c in ascii_result:
            hex_string += hex(ord(c))[2:]
        return hex_string.upper()


    def binary_combined_to_hex(self, input_string: str) -> str:
        ascii_result = Binary.binary_combined_to_ascii(self, input_string)
        hex_combined_string = ''
        for c in ascii_result:
            hex_combined_string += hex(ord(c))[2:]
        return hex_combined_string.upper()

    #TODO
    def binary_seperated_to_octal(self, input_string: str) -> str:
        pass

    #TODO
    def binary_combined_to_octal(self, input_string: str) -> str:
        pass


    def binary_converted_separated(self, input_string: str) -> dict:

        sep_results = {}
        sep_results['type'] = 'binary'
        sep_results['input'] = f'{input_string}'

        ascii = Binary.binary_separated_to_ascii(self, input_string)
        sep_results['ASCII'] = f'{ascii}'

        base64 = Binary.binary_separated_to_base64(self, input_string)
        sep_results['Base64'] = f'{base64}'

        decimal = Binary.binary_separated_to_dec(self, input_string)
        sep_results['Decimal'] = f'{decimal}'

        hexadecimal = Binary.binary_separated_to_hex(self, input_string)
        sep_results['Hexadecimal'] = f'{hexadecimal}'

        octal = Binary.binary_seperated_to_octal(self, input_string)
        sep_results['Octal'] = f'{octal}'

        return sep_results


    def binary_convert_combined(self, input_string: str) -> dict:

        combined_results = {}
        combined_results['type'] = 'binary'
        combined_results['input'] = f'{input_string}'

        ascii = Binary.binary_combined_to_ascii(self, input_string)
        combined_results['ASCII'] = f'{ascii}'

        base64 = Binary.binary_combined_to_base64(self, input_string)
        combined_results['Base64'] = f'{base64}'

        decimal = Binary.binary_combined_to_dec(self, input_string)
        combined_results['Decimal'] = f'{decimal}'

        hexadecimal = Binary.binary_combined_to_hex(self, input_string)
        combined_results['Hexadecimal'] = f'{hexadecimal}'

        octal = Binary.binary_combined_to_octal(self, input_string)
        combined_results['Octal'] = f'{octal}'

        return combined_results


    def print_binary_separated_output_panels(self,
                                             input_string: str) -> None:
        sep_results = Binary.binary_converted_separated(self, input_string)
        Results.print_results_panels(self, results_dict=sep_results)


    def print_binary_separated_output_table(self,
                                            input_string: str) -> None:
        sep_results = Binary.binary_converted_separated(self, input_string)
        Results.print_results_table(self, results_dict=sep_results)


    def print_binary_combined_output_panels(self,
                                            input_string: str) -> None:
        combined_results = Binary.binary_convert_combined(self, input_string)
        Results.print_results_panels(self, results_dict=combined_results)


    def print_binary_combined_output_table(self,
                                           input_string: str) -> None:
        combined_results = Binary.binary_convert_combined(self, input_string)
        Results.print_results_table(self, results_dict=combined_results)