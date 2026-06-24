# !/usr/bin/env python3

import base64
from results import Results


class Binary:
    """Utility class for binary conversions."""


    def __init__(self, data_type, results):
        self.data_type = data_type
        self.results = results


    def _validate(self, input_string: str) -> str:
        """Validates that the input is a non-empty binary string.
        Returns the cleaned string.
        """
        if not isinstance(input_string, str):
            raise TypeError("Input must be a string.")
        # Check for empty input value
        if not input_string:
            raise ValueError("Input can not be empty.")
        # Check to make sure the input consists of only 0 or 1
        if any (c not in "01" for c in input_string):
            raise ValueError("Binary input must be only 0 or 1.")
        return input_string


    def binary_to_ascii(self, input_string: str) -> str:
        list = []
        for i in range(0, len(input_string), 8):
            list.append(input_string[i:i+8])
        # ascii_combined_string = "".join([chr(int(i, 2)) for i in list])
        # return ascii_combined_string
        ascii_string = "".join([chr(int(i, 2)) for i in list])
        return ascii_string


    def binary_to_base64(self, input_string: str) -> str:
        """Converts a binary string (0s and 1s) to Base64."""
        binary_string = self._validate(input_string)
        # Pad binary string so length is multiple of 8
        padding_length = (8 - len(binary_string) % 8) % 8
        binary_string += "0" * padding_length
        # Convert binary string to bytes
        byte_array = bytearray()
        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))
        # Encode to base64
        b64_result = base64.b64encode(byte_array).decode("utf-8")
        return b64_result


    def binary_to_decimal(self, input_string: str) -> int:
        """Converts a binary string to a decimal integer."""
        binary_string = self._validate(input_string)
        decimal_value = f"{int(binary_string, 2):,}"
        return decimal_value


    def binary_to_hexadecimal(self, input_string: str) -> str:
        """Converts a binary string to a hexadecimal integer."""
        binary_string = self._validate(input_string)
        decimal_value = int(binary_string, 2)
        hex_string = f"{decimal_value:X}"

        if len(hex_string) % 2 !=0:
            hex_string = "0" + hex_string

        formatted_hex = " ".join(hex_string[i:i+2] for i in range(0, len(hex_string), 2))

        return formatted_hex


    def binary_to_octal(self, input_string: str) -> str:
        """Converts a binary string to a octal integer."""
        binary_string = self._validate(input_string)
        octal_value = oct(int(binary_string, 2))[2:]
        return octal_value


    def make_data_dict(self, input_string: str) -> dict:
        self.results["type"] = "binary"
        self.results["user_input"] = f"{input_string}"
        self.results["ASCII"] = f"{self.binary_to_ascii(input_string)}"
        self.results["Base64"] = f"{self.binary_to_base64(input_string)}"
        self.results["Decimal"] = f"{self.binary_to_decimal(input_string)}"
        self.results["Hexadecimal"] = f"{self.binary_to_hexadecimal(input_string)}"
        self.results["Octal"] = f"{self.binary_to_octal(input_string)}"
        return self.results


    def print_binary_output(self, input_string: str) -> None:
        output = self.make_data_dict(input_string)
        Results.print_results_table(self,
                                    data_type=self.data_type,
                                    results_dict=output)