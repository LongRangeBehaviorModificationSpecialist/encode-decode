# !/usr/bin/env python3

from results import Results
from rich.prompt import Prompt
from rich.traceback import install


install(show_locals=True)


class Octal:


    def octal_to_binary(self, input: str) -> str:
        """Converts an octal string to binary.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The binary equivalent of the octal numbers.
        """
        octal_list = input.split()
        binary_results = []
        for n in octal_list:
            # Convert octal string to decimal integer
            decimal_val = int(n, 8)
            # Convert decimal to binary
            # [2:] removes the '0b' prefix, zfill(8) ensures 8-bit padding
            binary_val = bin(decimal_val)[2:].zfill(8)
            binary_results.append(binary_val)
        return " ".join(binary_results)


    def octal_to_decimal(self, input: str) -> str:
        """Converts an octal string to a decimal integer.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The decimal equivalent of the octal numbers.
        """
        decimal_vals = [int(num, 8) for num in input.split()]
        return " ".join(map(str, decimal_vals))


    def octal_to_hexadecimal(self, input: str) -> str:
        """Converts an octal string to hexadecimal.

        Args:
            input_string: A string of octal numbers.

        Returns:
            The hexadecimal representation of the octal numbers.
        """
        octal_list = input.split()
        hex_number = [hex(int(num, 8))[2:].upper() for num in octal_list]
        return " ".join(hex_number)


    def make_data_dict(self, input: str) -> dict:
        results = {}
        results["Input Type"] = "Octal"
        results["Input Value"] = f"{input}"
        results["binary"] = f"{self.octal_to_binary()}"
        results["decimal"] = f"{self.octal_to_decimal()}"
        results["hexadecimal"] = f"{self.octal_to_hexadecimal()}"
        return results


    def run_octal_convert(self) -> None:
        input = Prompt.ask(
            f"[white][-] Enter the data you want to convert"
        )
        results = self.make_data_dict(input=input)
        Results.print_results_table(self, results_dict=results)
