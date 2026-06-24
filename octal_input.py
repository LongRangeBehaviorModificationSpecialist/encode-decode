# !/usr/bin/env python3

from results import Results


class Octal:


    def __init__(self, data_type, results):
        self.data_type = data_type
        self.results = results


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


    def make_data_dict(self, input_num: str) -> dict:
        self.results["type"] = "Octal"
        self.results["user_input"] = f"{input_num}"
        self.results["Binary"] = f"{self.octal_to_binary(input_num)}"
        self.results["Decimal"] = f"{self.octal_to_decimal(input_num)}"
        self.results["Hexadecimal"] = f"{self.octal_to_hexadecimal(input_num)}"
        return self.results


    def print_octal_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    data_type=self.data_type,
                                    results_dict=output)
