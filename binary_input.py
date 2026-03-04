# !/usr/bin/env python3

import base64
from results import Results


class Binary:
    """Utility class for binary conversions."""

    def _validate(self, input_string: str) -> str:
        """Validates that the input is a non-empty binary string.
        Returns the cleaned string."""

        if not isinstance(input_string, str):
            raise TypeError("Input must be a string.")

        binary_string = input_string.strip()

        # Check for empty input value
        if not binary_string:
            raise ValueError("Input can not be empty.")

        # Check to make sure the input consists of only 0 or 1
        if any (c not in "01" for c in binary_string):
            raise ValueError("Binary input must be only 0 or 1.")

        return binary_string


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

        binary_string = Binary._validate(self, input_string)

        # Pad binary string so length is multiple of 8
        padding_length = (8 - len(binary_string) % 8) % 8
        binary_string += "0" * padding_length

        # Convert binary string to bytes
        byte_array = bytearray()

        for i in range(0, len(binary_string), 8):
            byte = binary_string[i:i+8]
            byte_array.append(int(byte, 2))

        # Encode to Base64
        b64_result = base64.b64encode(byte_array).decode("utf-8")

        return b64_result


    def binary_to_decimal(self, input_string: str) -> int:
        """Converts a binary string to a decimal integer."""
        binary_string = Binary._validate(self, input_string)
        decimal_value = int(binary_string, 2)
        return decimal_value


    def binary_to_hexadecimal(self, input_string: str) -> str:
        """Converts a binary string to a hexadecimal integer."""
        binary_string = Binary._validate(self, input_string)
        hex_string = hex(int(binary_string, 2))[2:]
        return hex_string


    def binary_to_octal(self, input_string: str) -> str:
        """Converts a binary string to a octal integer."""
        binary_string = Binary._validate(self, input_string)
        octal_value = oct(int(binary_string, 2))[2:]
        return octal_value


    def make_data_dict(self, input_string: str) -> dict:

        combined_results = {}
        combined_results["type"] = "binary"
        combined_results["input"] = f"{input_string}"

        ascii = Binary.binary_to_ascii(self, input_string)
        combined_results["ASCII"] = f"{ascii}"

        base64 = Binary.binary_to_base64(self, input_string)
        combined_results["Base64"] = f"{base64}"

        decimal = Binary.binary_to_decimal(self, input_string)
        combined_results["Decimal"] = f"{decimal}"

        hexadecimal = Binary.binary_to_hexadecimal(self, input_string)
        combined_results["Hexadecimal"] = f"{hexadecimal}"

        octal = Binary.binary_to_octal(self, input_string)
        combined_results["Octal"] = f"{octal}"

        return combined_results


    def print_binary_output(self, input_string: str) -> None:
        combined_results = Binary.make_data_dict(self, input_string)
        Results.print_results_table(self,
                                    format="Binary",
                                    results_dict=combined_results)