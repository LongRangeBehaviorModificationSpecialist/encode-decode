# !/usr/bin/env python3

from results import Results


class Octal:


    def __init__(self, input_string: str, results: dict):
        self.input_string = input_string
        self.results = results


    def octal_to_binary(self) -> str:
        """
        Converts an octal string to binary.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The binary equivalent of the octal numbers.
        """
        octal_list = self.input_string.split()
        binary_results = []
        for n in octal_list:
            # Convert octal string to decimal integer
            decimal_val = int(n, 8)
            # Convert decimal to binary
            # [2:] removes the '0b' prefix, zfill(8) ensures 8-bit padding
            binary_val = bin(decimal_val)[2:].zfill(8)
            binary_results.append(binary_val)
        return " ".join(binary_results)


    def octal_to_decimal(self) -> str:
        """
        Converts an octal string to a decimal integer.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The decimal equivalent of the octal numbers.
        """
        decimal_vals = [int(num, 8) for num in self.input_string.split()]
        return " ".join(map(str, decimal_vals))


    def octal_to_hexadecimal(self) -> str:
        """
        Converts an octal string to hexadecimal.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The hexadecimal representation of the octal numbers.
        """
        octal_list = self.input_string.split()
        hex_number = [hex(int(num, 8))[2:].upper() for num in octal_list]
        return " ".join(hex_number)


    def make_data_dict(self) -> dict:
        self.results["type"] = "Octal"
        self.results["user_input"] = f"{self.input_string}"
        self.results["Binary"] = f"{self.octal_to_binary()}"
        self.results["Decimal"] = f"{self.octal_to_decimal()}"
        self.results["Hexadecimal"] = f"{self.octal_to_hexadecimal()}"
        return self.results


    def print_octal_output(self) -> None:
        results_dict = self.make_data_dict()
        Results.print_results_table(self, results_dict=results_dict)
