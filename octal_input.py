# !/usr/bin/env python3

from results import Results


class Octal:

    def octal_to_binary(self, input_num: int) -> int:
        '''Converts an octal string to binary.

        Args:
          input_num: An octal number.

        Returns:
          The binary equivalent of the octal number.
        '''
        binary_number = bin(int(str(input_num), 8))
        return binary_number[2:]


    def octal_to_decimal(self, input_num: int) -> int:
        '''Converts an octal string to a decimal integer.

        Args:
          input_num: An octal number.

        Returns:
          The decimal equivalent of the octal number.
        '''
        decimal_num = 0
        for digit in input_num:
            decimal_num = (decimal_num * 8) + int(digit)
        return decimal_num


    def octal_to_hexadecimal(self, input_num: int) -> int:
        '''Converts an octal string to hexadecimal.

        Args:
          input_num: The octal number.

        Returns:
          The hexadecimal representation of the octal number.
        '''
        hex_number = hex(int(input_num, 8))[2:].upper()
        return hex_number


    def octal_convert_all(self, input_num: str) -> dict:

        results = {}
        results['type'] = 'Octal'
        results['input'] = f'{input_num}'

        binary = Octal.octal_to_binary(self, input_num)
        results['Binary'] = f'{binary}'

        decimal = Octal.octal_to_decimal(self, input_num)
        results['Decimal'] = f'{decimal}'

        hexadecimal = Octal.octal_to_hexadecimal(self, input_num)
        results['Hexadecimal'] = f'{hexadecimal}'

        return results


    def print_octal_output_panels(self,
                                  input_string: str) -> None:
        results = Octal.octal_convert_all(self, input_string)
        Results.print_results_panels(self, results_dict=results)


    def print_octal_output_table(self,
                                 input_string: str) -> None:
        results = Octal.octal_convert_all(self, input_string)
        Results.print_results_table(self, results_dict=results)
