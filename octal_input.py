# !/usr/bin/env python3

from results import Results


class Octal:

    def octal_to_binary(self, input_string: int) -> int:
        """Converts an octal string to binary.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The binary equivalent of the octal numbers.
        """
        octal_list = input_string.split()

        binary_results = []

        for n in octal_list:
            # Convert octal string to decimal integer
            decimal_val = int(n, 8)

            # Convert decimal to binary
            # [2:] removes the '0b' prefix, zfill(8) ensures 8-bit padding
            binary_val = bin(decimal_val)[2:].zfill(8)

            binary_results.append(binary_val)

        return " ".join(binary_results)


    def octal_to_decimal(self, input_string: int) -> int:
        """Converts an octal string to a decimal integer.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The decimal equivalent of the octal numbers.
        """
        decimal_vals = [int(num, 8) for num in input_string.split()]

        decimal_string = " ".join(map(str, decimal_vals))

        return decimal_string


    def octal_to_hexadecimal(self, input_string: int) -> int:
        """Converts an octal string to hexadecimal.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The hexadecimal representation of the octal numbers.
        """
        octal_list = input_string.split()
        hex_number = [hex(int(num, 8))[2:].upper() for num in octal_list]

        hex_string = " ".join(hex_number)

        return hex_string


    def octal_convert_all(self, input_num: str) -> dict:

        results = {}
        results["type"] = "Octal"
        results["input"] = f"{input_num}"

        binary = Octal.octal_to_binary(self, input_num)
        results["Binary"] = f"{binary}"

        decimal = Octal.octal_to_decimal(self, input_num)
        results["Decimal"] = f"{decimal}"

        hexadecimal = Octal.octal_to_hexadecimal(self, input_num)
        results["Hexadecimal"] = f"{hexadecimal}"

        return results


    def print_octal_output(self, input_string: str) -> None:
        results = Octal.octal_convert_all(self, input_string)
        Results.print_results_table(self,
                                    format="Octal",
                                    results_dict=results)
